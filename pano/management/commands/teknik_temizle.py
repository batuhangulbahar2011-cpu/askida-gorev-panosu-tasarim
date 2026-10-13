from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from pano.models import Code, LoginAttempt
class Command(BaseCommand):
    help = 'Süresi dolmuş kodları ve geçici giriş sayaçlarını temizler.'
    def handle(self, *args, **options):
        Code.objects.filter(expires_at__lte=timezone.now()).delete()
        LoginAttempt.objects.filter(expires_at__lte=timezone.now()).delete()
        self.stdout.write('Süresi dolmuş teknik kayıtlar temizlendi.')
