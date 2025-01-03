from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = "Cria usuários padrão."

    def handle(self, *args, **kwargs):
        User = get_user_model()

        # Criação do usuário padrão
        if not User.objects.filter(username='user').exists():
            user = User.objects.create_user(username='user', password='L0XuwPOdS5U')
            user.role = 'user'
            user.save()
            self.stdout.write(self.style.SUCCESS('Usuário "user" criado com sucesso.'))

        # Criação do admin padrão
        if not User.objects.filter(username='admin').exists():
            admin = User.objects.create_user(username='admin', password='JKSipm0YH')
            admin.role = 'admin'
            admin.is_staff = True
            admin.is_superuser = True
            admin.save()
            self.stdout.write(self.style.SUCCESS('Usuário "admin" criado com sucesso.'))
