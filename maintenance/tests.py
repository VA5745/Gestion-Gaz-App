from django.test import TestCase
from equipment.models import Device
from .models import MaintenanceRecord
from datetime import date

class MaintenanceRecordTest(TestCase):
    def test_str(self):
        device = Device.objects.create(brand="Test", model="X1", serial_number="123", gas_types="O2", sensor_types="Electrochemical")
        record = MaintenanceRecord(device=device, date=date.today())
        self.assertIn(str(device), str(record))
