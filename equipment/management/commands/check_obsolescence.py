from django.core.management.base import BaseCommand
from equipment.models import Device
from datetime import date

class Command(BaseCommand):
    help = "Check devices nearing or past end of life"

    def handle(self, *args, **options):
        today = date.today()
        devices = Device.objects.filter(end_of_life_date__isnull=False)
        for device in devices:
            if device.is_obsolete():
                self.stdout.write(f"{device} is obsolete!")
            elif device.is_near_obsolescence():
                days = (device.end_of_life_date - today).days
                self.stdout.write(f"{device} expires in {days} days")
