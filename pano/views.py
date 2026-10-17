import hashlib
from datetime import timedelta
from functools import wraps
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError, OperationalError, transaction
from django.db.models import Q, F
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.views.decorators.cache import never_cache
from .forms import ActionForm, RegisterForm, RequestForm, ResetForm
from .models import Application, Code, Event, Flag, LoginAttempt, Notification, Period, Request, User
from .services import PRIVATE_ACTIONS, Conflict, RuleError, act, change_member, close_period, consume_code, event, issue_code, open_period

def advisor_only(view):
    @wraps(view)
    @login_required
    def wrapped(request, *args, **kwargs):
        if request.user.role != 'danisman':
            raise PermissionDenied
        return view(request, *args, **kwargs)
    return wrapped

def attempt_key(username):
    return hashlib.sha256(username.lower().encode()).hexdigest()

def throttled(key):
    return LoginAttempt.objects.filter(key=key, expires_at__gt=timezone.now(), count__gte=8).exists()

def fail_attempt(key):
    with transaction.atomic():
        row, _ = LoginAttempt.objects.get_or_create(key=key, defaults={'expires_at': timezone.now() + timedelta(minutes=15)})
        if row.expires_at <= timezone.now():
            row.count, row.expires_at = 0, timezone.now() + timedelta(minutes=15)
            row.save()
        LoginAttempt.objects.filter(pk=row.pk).update(count=F('count') + 1)

@never_cache
def sign_in(request):
    if request.user.is_authenticated:
        return redirect('board')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '').strip().lower()[:30]
        key = attempt_key(username)
        if throttled(key):
            error = 'Çok fazla deneme yapıldı. 15 dakika sonra tekrar deneyin.'
        else:
            user = authenticate(request, username=username, password=request.POST.get('password', ''))
            if user:
                LoginAttempt.objects.filter(key=key).delete()
                login(request, user)
                return redirect('board')
            fail_attempt(key)
            error = 'Kullanıcı adı veya parola hatalı.'
    return render(request, 'pano/login.html', {'error': error, 'setup_needed': not User.objects.exists()})

@never_cache
def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        key = attempt_key('register:' + form.cleaned_data['username'])
        try:
            if throttled(key):
                raise RuleError('Çok fazla deneme. 15 dakika sonra tekrar deneyin.')
            with transaction.atomic():
                open_period()
                consume_code(form.cleaned_data['code'], 'registration')
                user = User.objects.create_user(username=form.cleaned_data['username'], name=form.cleaned_data['name'], password=form.cleaned_data['password'], role='uye')
            LoginAttempt.objects.filter(key=key).delete()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('board')
        except (RuleError, OperationalError, IntegrityError) as exc:
            fail_attempt(key)
            form.add_error(None, str(exc) if isinstance(exc, RuleError) else 'İşlem şu anda meşgul. Tekrar deneyin.')
    return render(request, 'pano/form.html', {'form': form, 'title': 'Davetle kayıt ol', 'intro': 'Danışmanın verdiği tek kullanımlık kodla üye olabilirsiniz.', 'button': 'Kayıt ol'})

@never_cache
def reset_password(request):
    form = ResetForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        key = attempt_key('reset:' + form.cleaned_data['username'])
        try:
            if throttled(key):
                raise RuleError('Çok fazla deneme. 15 dakika sonra tekrar deneyin.')
            with transaction.atomic():
                target = User.objects.filter(username=form.cleaned_data['username'].lower(), is_active=True).first()
                if not target:
                    raise RuleError('Kod veya kullanıcı adı geçersiz.')
                consume_code(form.cleaned_data['code'], 'reset', target)
                target.set_password(form.cleaned_data['password'])
                target.save(update_fields=['password'])
            logout(request)
            messages.success(request, 'Parolanız yenilendi. Yeni parolanızla giriş yapın.')
            return redirect('login')
        except (RuleError, OperationalError) as exc:
            fail_attempt(key)
            form.add_error(None, str(exc) if isinstance(exc, RuleError) else 'İşlem meşgul. Tekrar deneyin.')
    return render(request, 'pano/form.html', {'form': form, 'title': 'Parolamı yenile', 'intro': 'Danışman kimliğinizi doğruladıktan sonra hesabınıza özel yenileme kodu verir.', 'button': 'Parolayı yenile'})

@require_POST
def sign_out(request):
    logout(request)
    return redirect('login')

def week_start():
    today = timezone.localdate()
    from datetime import datetime, time
    return timezone.make_aware(datetime.combine(today - timedelta(days=today.weekday()), time.min))

@login_required
def board(request):
    kind = request.GET.get('tur', 'gorev')
    if kind not in ['gorev', 'talep']:
        kind = 'gorev'
    items = Request.objects.filter(kind=kind).exclude(status='kapandi').select_related('owner', 'assignee').order_by(F('due_date').asc(nulls_last=True), 'created_at', 'pk')
    mine = request.GET.get('filtre', '')
    if mine == 'actiklarim':
        items = items.filter(owner=request.user)
    elif mine == 'ustlendiklerim':
        items = items.filter(assignee=request.user)
    state = request.GET.get('durum', '')
    if state not in ['acik', 'ustlenildi', 'onay_bekliyor']:
        state = ''
    if state:
        items = items.filter(status=state)
    query = request.GET.get('q', '').strip()[:100]
    if query:
        items = items.filter(title__icontains=query)
    approved = Event.objects.filter(action='onaylandi', created_at__gte=week_start())
    return render(request, 'pano/board.html', {'items': items, 'kind': kind, 'mine': mine, 'state': state, 'query': query, 'tasks_total': approved.filter(request__kind='gorev').count(), 'helps_total': approved.filter(request__kind='talep').count(), 'period': Period.objects.first()})

@login_required
def create_request(request):
    form = RequestForm(request.POST or None, user=request.user, initial={'kind': request.GET.get('tur', 'talep')})
    if request.method == 'POST' and form.is_valid():
        try:
            with transaction.atomic():
                open_period()
                item = form.save(commit=False)
                current = User.objects.get(pk=request.user.pk)
                if not current.is_active or (item.kind == 'gorev' and current.role not in ['kaptan', 'danisman']):
                    raise PermissionDenied
                item.owner = request.user
                item.save()
                event(item, request.user, 'acildi', 'İstek yayımlandı.')
            messages.success(request, 'İsteğiniz panoda yayımlandı.')
            return redirect('detail', item.pk)
        except RuleError as exc:
            form.add_error(None, str(exc))
    return render(request, 'pano/create.html', {'form': form})

@login_required
def edit_request(request, pk):
    item = get_object_or_404(Request, pk=pk)
    if item.owner_id != request.user.pk or item.status != 'acik':
        raise PermissionDenied
    original_date = item.due_date
    form = RequestForm(request.POST or None, instance=item, user=request.user)
    if request.method == 'POST' and form.is_valid():
        try:
            with transaction.atomic():
                open_period()
                changes = {key: form.cleaned_data[key] for key in ['title', 'description', 'team_purpose', 'due_date']}
                changed = Request.objects.filter(pk=pk, owner=request.user, status='acik', version=form.cleaned_data['version']).update(**changes, version=F('version') + 1)
                if not changed:
                    raise Conflict('İstek güncellendi. Yenileyip tekrar deneyin.')
                event(item, request.user, 'duzenlendi', form.cleaned_data.get('date_reason') or 'Başlık/açıklama düzenlendi.')
            return redirect('detail', pk)
        except (RuleError, Conflict) as exc:
            form.add_error(None, str(exc))
    return render(request, 'pano/form.html', {'form': form, 'title': 'İsteği düzenle', 'button': 'Kaydet'})

def detail_context(request, item):
    owner = item.owner_id == request.user.pk
    assigned = item.assignee_id == request.user.pk
    can_review = request.user.role == 'danisman' and not assigned and (item.flags.filter(state='acik').exists() or item.needs_review or item.overdue)
    can_see_offers = owner or (request.user.role == 'danisman' and item.flags.exists())
    offers = item.applications.select_related('user').all() if can_see_offers else item.applications.select_related('user').filter(user=request.user)
    events = item.events.select_related('actor', 'subject_user')
    if not can_see_offers:
        events = events.filter(~Q(action__in=PRIVATE_ACTIONS) | Q(subject_user=request.user, action__in=PRIVATE_ACTIONS))
    return {'item': item, 'owner': owner, 'assigned': assigned, 'offers': offers, 'events': events, 'comments': item.comments.select_related('author'), 'can_review': can_review, 'can_see_offers': can_see_offers, 'can_apply': item.status == 'acik' and not owner and not (item.kind == 'gorev' and request.user.role == 'danisman'), 'flags': item.flags.select_related('reporter') if request.user.role == 'danisman' else item.flags.filter(reporter=request.user), 'labels': {'acildi': 'İstek açıldı'}}

@login_required
def detail(request, pk):
    item = get_object_or_404(Request.objects.select_related('owner', 'assignee'), pk=pk)
    return render(request, 'pano/detail.html', detail_context(request, item))

@login_required
@require_POST
def action(request, pk):
    get_object_or_404(Request, pk=pk)
    form = ActionForm(request.POST)
    status = 400
    if form.is_valid():
        try:
            act(request.user, pk, **form.cleaned_data)
            messages.success(request, 'İşlem kaydedildi.')
            return redirect('detail', pk)
        except Conflict as exc:
            error, status = str(exc), 409
        except RuleError as exc:
            error = str(exc)
        except OperationalError:
            error, status = 'İşlem şu anda meşgul. Sayfayı yenileyip tekrar deneyin.', 409
    else:
        error = 'İşlem formu geçersiz. Not uzunluğunu kontrol edip sayfayı yenileyin.'
    item = Request.objects.select_related('owner', 'assignee').get(pk=pk)
    context = detail_context(request, item)
    context['action_error'] = error
    return render(request, 'pano/detail.html', context, status=status)

@login_required
def archive(request):
    result = request.GET.get('sonuc', 'onaylandi')
    if result not in ['onaylandi', 'geri_cekildi']:
        result = 'onaylandi'
    records = Event.objects.filter(action=result).select_related('request__owner', 'subject_user').order_by('-created_at', '-id')
    if request.GET.get('tur') in ['gorev', 'talep']:
        records = records.filter(request__kind=request.GET['tur'])
    kind = request.GET.get('tur', '')
    if kind not in ['gorev', 'talep']:
        kind = ''
    period = request.GET.get('donem', '')
    if period not in ['hafta', 'ay']:
        period = ''
    if period == 'hafta':
        records = records.filter(created_at__gte=week_start())
    elif period == 'ay':
        from datetime import datetime, time
        month_start = timezone.make_aware(datetime.combine(timezone.localdate().replace(day=1), time.min))
        records = records.filter(created_at__gte=month_start)
    return render(request, 'pano/archive.html', {'records': records, 'result': result, 'kind': kind, 'period_filter': period})

@login_required
def notifications(request):
    records = Notification.objects.filter(recipient=request.user).select_related('request').order_by('-created_at', '-pk')
    return render(request, 'pano/notifications.html', {'records': records})

@login_required
@require_POST
def read_notification(request, pk):
    row = get_object_or_404(Notification, pk=pk, recipient=request.user)
    Notification.objects.filter(pk=row.pk).update(read_at=timezone.now())
    return redirect('detail', row.request_id)

@advisor_only
def summary(request):
    recent = Event.objects.filter(created_at__gte=week_start())
    rows = []
    for person in User.objects.all():
        row = {'person': person}
        for prefix, kind in [('task', 'gorev'), ('help', 'talep')]:
            row[prefix + '_applications'] = recent.filter(action='adaylik', subject_user=person, request__kind=kind).values('request_id').distinct().count()
            row[prefix + '_accepted'] = recent.filter(action='ustlenildi', subject_user=person, request__kind=kind).values('request_id').distinct().count()
            row[prefix + '_approved'] = recent.filter(action='onaylandi', subject_user=person, request__kind=kind).count()
        rows.append(row)
    review = [item for item in Request.objects.exclude(status='kapandi').select_related('owner', 'assignee') if item.needs_review or item.overdue or item.flags.filter(state='acik').exists()]
    closed_flags = Request.objects.filter(status='kapandi', flags__state='acik').distinct()
    return render(request, 'pano/summary.html', {'rows': rows, 'review': review, 'closed_flags': closed_flags})

@advisor_only
@never_cache
def team(request):
    raw_code = None
    error = None
    if request.method == 'POST':
        try:
            with transaction.atomic():
                if not User.objects.filter(pk=request.user.pk, role='danisman', is_active=True).exists():
                    raise PermissionDenied
                command = request.POST.get('command')
                if command == 'invite':
                    open_period()
                    raw_code, _ = issue_code(request.user)
                elif command == 'reset':
                    person = get_object_or_404(User, pk=request.POST.get('person'), is_active=True)
                    if person.role == 'danisman':
                        raise RuleError('Danışman kurtarma kodunu Batu bakım komutuyla üretir.')
                    raw_code, _ = issue_code(request.user, person)
                elif command == 'revoke':
                    get_object_or_404(Code, pk=request.POST.get('code'), kind='registration')
                    Code.objects.filter(pk=request.POST['code'], used_at__isnull=True, revoked_at__isnull=True).update(revoked_at=timezone.now())
                elif command == 'member':
                    person = get_object_or_404(User, pk=request.POST.get('person'))
                    active = request.POST.get('active') == 'on'
                    if not active and request.POST.get('confirm') != 'on':
                        raise RuleError('Pasifleştirmeden önce işleri devretme onayını işaretleyin.')
                    change_member(request.user, person, request.POST.get('role'), active)
                elif command == 'close_period':
                    if request.POST.get('confirm') != 'on':
                        raise RuleError('90 günlük saklama süresini onaylayın.')
                    close_period(request.user)
                else:
                    raise RuleError('Geçersiz işlem.')
            if not raw_code:
                messages.success(request, 'Takım ayarı kaydedildi.')
                return redirect('team')
        except (RuleError, OperationalError) as exc:
            error = str(exc) if isinstance(exc, RuleError) else 'İşlem meşgul. Tekrar deneyin.'
    return render(request, 'pano/team.html', {'people': User.objects.all(), 'codes': Code.objects.filter(kind='registration').order_by('-created_at')[:20], 'raw_code': raw_code, 'error': error, 'period': Period.objects.first()})
