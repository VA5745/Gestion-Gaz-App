from django.test import TestCase
from django.core.management import call_command
from io import StringIO
from datetime import date, timedelta
from .models import Device

class DeviceModelTest(TestCase):
    def test_str(self):
        device = Device(
            brand="Test",
            model="X1",
            serial_number="123",
            gas_types="O2",
            sensor_types="Electrochemical",
        )
        self.assertEqual(str(device), "Test X1 (123)")

    def test_obsolescence_flags(self):
        today = date.today()
        device = Device(
            brand="Test",
            model="X1",
            serial_number="124",
            gas_types="O2",
            sensor_types="Electrochemical",
            end_of_life_date=today + timedelta(days=10),
        )
        self.assertFalse(device.is_obsolete())
        self.assertTrue(device.is_near_obsolescence())

    def test_check_obsolescence_command(self):
        device = Device.objects.create(
            brand="Test",
            model="X1",
            serial_number="125",
            gas_types="O2",
            sensor_types="Electrochemical",
            end_of_life_date=date.today() - timedelta(days=1),
        )
        out = StringIO()
        call_command("check_obsolescence", stdout=out)
        self.assertIn("obsolete", out.getvalue())
