from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = "Create default user roles"

    def handle(self, *args, **options):
        roles = ["Admin", "Technicien", "Client", "Manager"]
        for role in roles:
            Group.objects.get_or_create(name=role)
        self.stdout.write(self.style.SUCCESS("Roles created"))
