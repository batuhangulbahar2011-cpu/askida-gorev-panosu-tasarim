import hashlib
import secrets
from datetime import timedelta
from django.core.exceptions import PermissionDenied
from django.db import transaction
from django.db.models import F
from django.utils import timezone
from .models import Application, Code, Event, Flag, Notification, Period, Request, User

PRIVATE_ACTIONS = ['adaylik', 'adaylik_geri_cekildi', 'secilmedi', 'kabul_notu']
class Conflict(Exception):
    pass
class RuleError(Exception):
    pass

def open_period():
    if Period.objects.filter(period_closed_at__isnull=False).exists():
        raise RuleError('Dönem kapalı; yeni işlem yapılamaz. Danışmana haber verin.')

def issue_code(actor=None, target=None):
    raw = secrets.token_urlsafe(18)
    with transaction.atomic():
        if target:
            Code.objects.filter(kind='reset', user=target, used_at__isnull=True, revoked_at__isnull=True).update(revoked_at=timezone.now())
        code = Code.objects.create(code_hash=hashlib.sha256(raw.encode()).hexdigest(), kind='reset' if target else 'registration', user=target, created_by=actor, expires_at=timezone.now() + (timedelta(hours=24) if target else timedelta(days=7)))
    return raw, code

def consume_code(raw, kind, target=None):
    qs = Code.objects.filter(code_hash=hashlib.sha256(raw.strip().encode()).hexdigest(), kind=kind, user=target, used_at__isnull=True, revoked_at__isnull=True, expires_at__gt=timezone.now())
    code = qs.first()
    if not code or qs.update(used_at=timezone.now()) != 1:
        raise RuleError('Kod geçersiz, süresi dolmuş veya kullanılmış.')
    return code

def notify(person, item, kind):
    if person:
        Notification.objects.create(recipient=person, request=item, kind=kind)

def event(item, actor, action, note='', subject=None):
    return Event.objects.create(request=item, actor=actor, action=action, note=note, subject_user=subject)

@transaction.atomic
def act(actor, item_id, version, action, note='', target=None):
    actor = User.objects.filter(pk=actor.pk, is_active=True).first()
    if not actor:
        raise PermissionDenied
    open_period()
    item = Request.objects.select_related('owner', 'assignee').get(pk=item_id)
    if item.version != version:
        raise Conflict('Bu istek güncellendi. Sayfayı yenileyip tekrar deneyin.')
    owner = item.owner_id == actor.pk
    assigned = item.assignee_id == actor.pk
    note = note.strip()
    advisor_actions = ['advisor_approve', 'advisor_correct', 'advisor_reopen', 'advisor_cancel', 'resolve_flag', 'clean_comment']
    advisor = action in advisor_actions
    if advisor:
        if actor.role != 'danisman' or assigned:
            raise PermissionDenied
        if not (item.flags.exists() or item.needs_review or item.overdue):
            raise RuleError('Danışman kararı için bildirim, gecikme veya 48 saat aşımı gerekir.')
    needed = ['accept', 'done', 'correct', 'leave', 'cancel', 'flag', 'comment'] + advisor_actions
    if action in needed and not note:
        raise RuleError('Bu işlem için kısa bir not veya gerekçe yazın.')
    if len(note) > 1000:
        raise RuleError('Not en fazla 1000 karakter olabilir.')
    # Sürümü koşullu artırmak, aynı anda iki kabul/onay oluşmasını engeller.
    if Request.objects.filter(pk=item.pk, version=version).update(version=F('version') + 1) != 1:
        raise Conflict('Bu istek güncellendi. Sayfayı yenileyin.')
    if action == 'apply':
        if item.status != 'acik' or owner or (item.kind == 'gorev' and actor.role == 'danisman'):
            raise PermissionDenied
        if len(note) > 300:
            raise RuleError('Teklif notu en fazla 300 karakter olabilir.')
        row, _ = Application.objects.get_or_create(request=item, user=actor)
        if row.state == 'bekliyor' and row.note == note and not _:
            raise RuleError('Teklifiniz zaten bekliyor.')
        row.state, row.note, row.updated_at = 'bekliyor', note, timezone.now()
        row.save()
        event(item, actor, 'adaylik', note, actor)
        notify(item.owner, item, 'yeni_teklif')
    elif action == 'withdraw':
        row = Application.objects.filter(request=item, user=actor, state='bekliyor').first()
        if item.status != 'acik' or not row:
            raise PermissionDenied
        row.state = 'geri_cekildi'
        row.save(update_fields=['state'])
        event(item, actor, 'adaylik_geri_cekildi', subject=actor)
    elif action == 'accept':
        if not owner or item.status != 'acik':
            raise PermissionDenied
        row = Application.objects.filter(pk=target, request=item, state='bekliyor', user__is_active=True).select_related('user').first()
        if not row or row.user_id == actor.pk or (item.kind == 'gorev' and row.user.role == 'danisman'):
            raise RuleError('Bu teklif artık kabul edilemez.')
        others = list(Application.objects.filter(request=item, state='bekliyor').exclude(pk=row.pk).select_related('user'))
        Application.objects.filter(pk__in=[r.pk for r in others]).update(state='secilmedi')
        for other in others:
            event(item, actor, 'secilmedi', subject=other.user)
            notify(other.user, item, 'secilmedi')
        row.state = 'kabul'
        row.save(update_fields=['state'])
        item.assignee, item.status = row.user, 'ustlenildi'
        event(item, actor, 'kabul_notu', note, row.user)
        event(item, actor, 'ustlenildi', 'İstek bir kişi tarafından üstlenildi.', row.user)
        notify(row.user, item, 'kabul')
    elif action == 'done':
        if not assigned or item.status != 'ustlenildi':
            raise PermissionDenied
        item.status = 'onay_bekliyor'
        event(item, actor, 'yapildi', note, actor)
        notify(item.owner, item, 'yapildi')
    elif action in ['approve', 'advisor_approve']:
        if (not owner and not advisor) or assigned or item.status != 'onay_bekliyor':
            raise PermissionDenied
        item.status = 'kapandi'
        event(item, actor, 'onaylandi', note, item.assignee)
        notify(item.assignee, item, 'onaylandi')
    elif action in ['correct', 'advisor_correct']:
        if (not owner and not advisor) or item.status != 'onay_bekliyor':
            raise PermissionDenied
        item.status = 'ustlenildi'
        event(item, actor, 'duzeltme', note, item.assignee)
        notify(item.assignee, item, 'duzeltme')
    elif action in ['leave', 'advisor_reopen']:
        if (not assigned and not advisor) or item.status not in ['ustlenildi', 'onay_bekliyor']:
            raise PermissionDenied
        previous = item.assignee
        item.status, item.assignee = 'acik', None
        Application.objects.filter(request=item, state__in=['bekliyor', 'kabul']).update(state='geri_cekildi')
        event(item, actor, 'birakildi', note, previous)
        notify(item.owner, item, 'birakildi')
    elif action in ['cancel', 'advisor_cancel']:
        if (not owner and not advisor) or item.status == 'kapandi':
            raise PermissionDenied
        item.status = 'kapandi'
        Application.objects.filter(request=item, state='bekliyor').update(state='geri_cekildi')
        event(item, actor, 'geri_cekildi', note, item.assignee)
        notify(item.assignee, item, 'geri_cekildi')
    elif action == 'comment':
        item.comments.create(author=actor, body=note)
    elif action == 'flag':
        if len(note) > 500:
            raise RuleError('Bildirim en fazla 500 karakter olabilir.')
        if item.flags.filter(reporter=actor, state='acik').exists():
            raise RuleError('Bu isteğe ilişkin bildiriminiz zaten inceleme bekliyor.')
        Flag.objects.create(request=item, reporter=actor, reason=note)
    elif action == 'resolve_flag':
        if not item.flags.filter(state='acik').exists():
            raise RuleError('Açık bildirim yok.')
        event(item, actor, 'danisman_karari', note)
    elif action == 'clean_comment':
        comment = item.comments.filter(pk=target).first()
        if not comment:
            raise RuleError('Yorum bulunamadı.')
        comment.body = '[Danışman tarafından kişisel veriden arındırıldı.]'
        comment.save(update_fields=['body'])
        event(item, actor, 'yorum_temizlendi', note)
    else:
        raise RuleError('Geçersiz işlem.')
    if advisor:
        item.flags.filter(state='acik').update(state='cozuldu')
        if action != 'resolve_flag':
            event(item, actor, 'danisman_karari', note)
    item.save(update_fields=['status', 'assignee'])
    return item

@transaction.atomic
def change_member(actor, person, role, active):
    actor = User.objects.filter(pk=actor.pk, role='danisman', is_active=True).first()
    if not actor:
        raise PermissionDenied
    if role not in ['uye', 'kaptan', 'danisman']:
        raise RuleError('Geçersiz rol.')
    person = User.objects.get(pk=person.pk)
    if person.role == 'danisman' and person.is_active and (not active or role != 'danisman'):
        if User.objects.filter(role='danisman', is_active=True).exclude(pk=person.pk).count() == 0:
            raise RuleError('Son aktif danışman pasifleştirilemez veya başka role indirilemez.')
    old = person.get_role_display()
    if person.is_active and not active:
        replacement = User.objects.filter(role='danisman', is_active=True).exclude(pk=person.pk).first()
        if not replacement:
            raise RuleError('İstekleri devralacak aktif danışman gerekiyor.')
        for item in Request.objects.filter(assignee=person).exclude(status='kapandi'):
            Request.objects.filter(pk=item.pk).update(status='acik', assignee=None, version=F('version') + 1)
            Application.objects.filter(request=item, state__in=['kabul', 'bekliyor']).update(state='geri_cekildi')
            event(item, actor, 'birakildi', 'Üyelik pasifleştirildi; istek yeniden açıldı.', person)
            notify(item.owner, item, 'birakildi')
        for item in Request.objects.filter(owner=person).exclude(status='kapandi'):
            if item.assignee_id == replacement.pk:
                Request.objects.filter(pk=item.pk).update(status='acik', assignee=None)
                Application.objects.filter(request=item, state__in=['kabul', 'bekliyor']).update(state='geri_cekildi')
                event(item, actor, 'birakildi', 'Sahiplik devrinde onaylayan ve üstlenen ayrıldı.', replacement)
            Request.objects.filter(pk=item.pk).update(owner=replacement, version=F('version') + 1)
            event(item, actor, 'sahiplik_devri', 'Pasif hesabın isteği danışmana devredildi.', person)
        Application.objects.filter(user=person, state='bekliyor').update(state='geri_cekildi')
        Code.objects.filter(user=person, used_at__isnull=True).update(revoked_at=timezone.now())
        from django.contrib.sessions.models import Session
        for session in Session.objects.filter(expire_date__gt=timezone.now()):
            if session.get_decoded().get('_auth_user_id') == str(person.pk):
                session.delete()
    person.role, person.is_active = role, active
    person.save(update_fields=['role', 'is_active'])
    event(None, actor, 'uyelik_degisti', f'{old} → {person.get_role_display()}; aktif: {active}', person)

@transaction.atomic
def close_period(actor):
    if not User.objects.filter(pk=actor.pk, role='danisman', is_active=True).exists():
        raise PermissionDenied
    if Request.objects.exclude(status='kapandi').exists():
        raise RuleError('Aktif istekler kapanmadan dönem kapatılamaz.')
    period, _ = Period.objects.get_or_create(pk=1)
    if period.period_closed_at:
        raise RuleError('Dönem zaten kapalı.')
    period.period_closed_at = timezone.now()
    period.purge_after = period.period_closed_at + timedelta(days=90)
    period.save()
