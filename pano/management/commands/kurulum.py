from getpass import getpass
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from pano.models import User

class Command(BaseCommand):
    help = 'İlk danışman hesabını oluşturur; mevcut hesaplara dokunmaz.'
    def handle(self, *args, **options):
        if User.objects.exists():
            self.stdout.write('Kurulum daha önce tamamlandı; mevcut hesaplar korundu.')
            return
        self.stdout.write('İlk danışman hesabı. Danışman kendi parolasını belirlemeli.')
        username = input('Kullanıcı adı: ').strip().lower()
        name = input('Ad: ').strip()
        password = getpass('Parola (yazarken görünmez): ')
        if password != getpass('Parola tekrar: '):
            raise CommandError('Parolalar eşleşmedi.')
        user = User(username=username, name=name, role='danisman')
        try:
            user.full_clean(exclude=['password'])
            password_validation.validate_password(password, user)
        except ValidationError as exc:
            raise CommandError('; '.join(exc.messages))
        with transaction.atomic():
            if User.objects.exists():
                raise CommandError('Kurulum başka bir işlemde tamamlandı.')
            User.objects.create_user(username=username, name=name, password=password, role='danisman')
        self.stdout.write(self.style.SUCCESS('Danışman hesabı oluşturuldu. Giriş yaptıktan sonra Takım ekranından kayıt kodu üretin.'))
