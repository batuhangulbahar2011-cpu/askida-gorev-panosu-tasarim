from datetime import timedelta
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone

ROLES = [('uye', 'Üye'), ('kaptan', 'Kaptan'), ('danisman', 'Danışman')]
STATES = [('acik', 'Açık'), ('ustlenildi', 'Üstlenildi'), ('onay_bekliyor', 'Onay bekliyor'), ('kapandi', 'Kapandı')]

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra):
        user = self.model(username=username.lower(), **extra)
        user.set_password(password)
        user.full_clean(exclude=['password'])
        user.save(using=self._db)
        return user
    def create_superuser(self, username, password=None, **extra):
        extra.update(role='danisman', is_staff=True, is_superuser=True)
        return self.create_user(username, password, **extra)

class User(AbstractUser):
    username = models.CharField('Kullanıcı adı', max_length=30, unique=True, validators=[RegexValidator(r'^[a-zA-Z0-9_]{3,30}$', '3–30 harf, rakam veya alt çizgi kullanın.')])
    email = None
    first_name = None
    last_name = None
    name = models.CharField('Ad', max_length=60)
    role = models.CharField('Rol', max_length=10, choices=ROLES, default='uye')
    objects = UserManager()
    EMAIL_FIELD = 'name'
    REQUIRED_FIELDS = ['name']
    class Meta:
        ordering = ['name', 'id']
    def __str__(self):
        return self.name
    def get_full_name(self):
        return self.name
    def get_short_name(self):
        return self.name

class Request(models.Model):
    kind = models.CharField('Tür', max_length=5, choices=[('gorev', 'Takım görevi'), ('talep', 'Yardım talebi')])
    title = models.CharField('Başlık', max_length=100)
    description = models.TextField('Açıklama', max_length=2000)
    team_purpose = models.CharField('Takım için beklenen çıktı', max_length=500, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='owned_requests')
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True, related_name='assigned_requests')
    status = models.CharField(max_length=20, choices=STATES, default='acik')
    due_date = models.DateField('Son tarih', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    version = models.PositiveIntegerField(default=1)
    class Meta:
        constraints = [models.CheckConstraint(condition=(models.Q(status__in=['acik', 'kapandi']) | models.Q(assignee__isnull=False)), name='active_work_has_assignee')]
    @property
    def overdue(self):
        return self.status != 'kapandi' and self.due_date and self.due_date < timezone.localdate()
    @property
    def waiting_since(self):
        if self.status != 'onay_bekliyor':
            return None
        return self.events.filter(action='yapildi').order_by('-created_at', '-id').values_list('created_at', flat=True).first()
    @property
    def needs_review(self):
        since = self.waiting_since
        return bool(since and since <= timezone.now() - timedelta(hours=48))

class Application(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    note = models.CharField(max_length=300, blank=True)
    state = models.CharField(max_length=20, default='bekliyor', choices=[('bekliyor', 'Bekliyor'), ('kabul', 'Kabul edildi'), ('secilmedi', 'Bu istek için kişi belirlendi'), ('geri_cekildi', 'Geri çekildi')])
    updated_at = models.DateTimeField(default=timezone.now)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['request', 'user'], name='one_application_per_person')]

class Comment(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    body = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)

class Event(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='events', null=True)
    subject_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='subject_events', null=True)
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, related_name='actor_events')
    action = models.CharField(max_length=40)
    note = models.CharField(max_length=1000, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ['created_at', 'id']
        constraints = [models.UniqueConstraint(fields=['request'], condition=models.Q(action='onaylandi'), name='one_approval_per_request')]
    def save(self, *args, **kwargs):
        if self.pk:
            raise ValueError('Olaylar değiştirilemez; yeni düzeltme olayı yazın.')
        super().save(*args, **kwargs)
    @property
    def action_label(self):
        return {'acildi': 'İstek açıldı', 'adaylik': 'Teklif verildi', 'adaylik_geri_cekildi': 'Teklif geri çekildi', 'secilmedi': 'Bu istek için kişi belirlendi', 'kabul_notu': 'Seçim gerekçesi', 'ustlenildi': 'İstek üstlenildi', 'yapildi': 'Sonuç bildirildi', 'onaylandi': 'Sonuç onaylandı', 'duzeltme': 'Düzeltme istendi', 'birakildi': 'İstek yeniden açıldı', 'geri_cekildi': 'İstek geri çekildi', 'danisman_karari': 'Danışman incelemesi', 'yorum_temizlendi': 'Yorum kişisel veriden arındırıldı', 'duzenlendi': 'İstek düzenlendi', 'sahiplik_devri': 'İstek danışmana devredildi', 'uyelik_degisti': 'Üyelik güncellendi'}.get(self.action, 'İstek güncellendi')

class Flag(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='flags')
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    reason = models.CharField(max_length=500)
    state = models.CharField(max_length=10, default='acik')
    created_at = models.DateTimeField(default=timezone.now)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['request', 'reporter'], condition=models.Q(state='acik'), name='one_open_flag')]

class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    kind = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=timezone.now)
    read_at = models.DateTimeField(null=True)
    @property
    def text(self):
        return {'yeni_teklif': 'İsteğinize yeni bir teklif geldi.', 'kabul': 'Teklifiniz kabul edildi.', 'secilmedi': 'Bu istek için kişi belirlendi. Teklifiniz için teşekkür ederiz; başka bir isteğe teklif verebilirsiniz.', 'yapildi': 'İsteğinizin sonucu onayınızı bekliyor.', 'onaylandi': 'Tamamladığınız iş onaylandı.', 'duzeltme': 'İstek sahibi sonuçta düzeltme istedi.', 'birakildi': 'Üstlenen kişi işi bıraktı; istek yeniden açık.', 'geri_cekildi': 'İstek sahibi isteği geri çekti.'}.get(self.kind, 'İstek güncellendi.')

class Code(models.Model):
    code_hash = models.CharField(max_length=64, unique=True)
    kind = models.CharField(max_length=12, choices=[('registration', 'Kayıt'), ('reset', 'Parola yenileme')])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='reset_codes')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, related_name='issued_codes')
    created_at = models.DateTimeField(default=timezone.now)
    expires_at = models.DateTimeField()
    used_at = models.DateTimeField(null=True)
    revoked_at = models.DateTimeField(null=True)
    @property
    def available(self):
        return not self.used_at and not self.revoked_at and self.expires_at > timezone.now()

class Period(models.Model):
    period_closed_at = models.DateTimeField(null=True)
    purge_after = models.DateTimeField(null=True)

class LoginAttempt(models.Model):
    key = models.CharField(max_length=64, unique=True)
    count = models.PositiveIntegerField(default=0)
    expires_at = models.DateTimeField()
