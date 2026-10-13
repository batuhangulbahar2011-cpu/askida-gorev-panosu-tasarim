from django.core.management.base import BaseCommand, CommandError
from pano.models import User
from pano.services import issue_code

class Command(BaseCommand):
    help = 'Bakım sorumlusu kimlik doğrulamasından sonra danışmana 24 saatlik kod üretir.'
    def add_arguments(self, parser):
        parser.add_argument('username')
    def handle(self, *args, **options):
        user = User.objects.filter(username=options['username'].lower(), role='danisman', is_active=True).first()
        if not user:
            raise CommandError('Aktif danışman bulunamadı.')
        if input(f'{user.name} kişinin kimliğini doğruladınız mı? EVET yazın: ') != 'EVET':
            raise CommandError('Kimlik doğrulaması onaylanmadı.')
        raw, _ = issue_code(target=user)
        self.stdout.write('Yalnız bu danışmanın hesabı için 24 saat geçerli tek kullanımlık kod:')
        self.stdout.write(raw)
