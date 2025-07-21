from django.db import models
from datetime import date, timedelta

class Device(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    gas_types = models.CharField(max_length=200, help_text="Types de gaz détectés")
    sensor_types = models.CharField(max_length=200, help_text="Types de capteurs")
    warranty_end_date = models.DateField(null=True, blank=True, help_text="Fin de garantie")
    end_of_life_date = models.DateField(null=True, blank=True, help_text="Fin de vie (obsolescence)")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.serial_number})"

    def is_obsolete(self):
        return self.end_of_life_date is not None and self.end_of_life_date < date.today()

    def is_near_obsolescence(self):
        if self.end_of_life_date is None:
            return False
        today = date.today()
        return today <= self.end_of_life_date <= today + timedelta(days=30)
