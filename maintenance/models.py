from django.db import models
from equipment.models import Device

class MaintenanceRecord(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Maintenance for {self.device} on {self.date}"
