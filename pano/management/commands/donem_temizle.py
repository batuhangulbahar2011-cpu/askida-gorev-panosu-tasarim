from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from django.utils import timezone
from pano.models import Code, Event, LoginAttempt, Period, Request, User

class Command(BaseCommand):
    help = 'Dönem kapanışından 90 gün sonra kayıtları temizler. Varsayılan yalnız önizlemedir.'
    def add_arguments(self, parser):
        parser.add_argument('--uygula', action='store_true')
    def handle(self, *args, **options):
        period = Period.objects.first()
        ready = bool(period and period.purge_after and period.purge_after <= timezone.now())
        self.stdout.write(f'Dönem temizliğe hazır: {ready}. İstek sayısı: {Request.objects.count()}')
        if not options['uygula']:
            self.stdout.write('Değişiklik yapılmadı. --uygula temizliği gerçekleştirir.')
            return
        with transaction.atomic():
            if not ready:
                raise CommandError('90 günlük süre dolmadı; dönem kayıtları korunuyor.')
            if Request.objects.exclude(status='kapandi').exists():
                raise CommandError('Aktif istek var; temizleme durduruldu.')
            Request.objects.all().delete()
            Event.objects.filter(request__isnull=True).delete()
            Code.objects.all().delete()
            LoginAttempt.objects.all().delete()
            User.objects.filter(is_active=False).delete()
            Period.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Dönem temizlendi. Aktif hesaplar korundu; yeni dönem açıldı.'))
