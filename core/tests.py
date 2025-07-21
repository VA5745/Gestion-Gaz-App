from django.contrib.auth.models import Group
from django.core.management import call_command
from django.test import TestCase


class CreateRolesCommandTest(TestCase):
    def test_roles_created(self):
        call_command("create_roles")
        for role in ["Admin", "Technicien", "Client", "Manager"]:
            self.assertTrue(Group.objects.filter(name=role).exists())
