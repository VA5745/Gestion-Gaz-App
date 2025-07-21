from django.contrib import admin
from .models import Device

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = (
        "brand",
        "model",
        "serial_number",
        "warranty_end_date",
        "end_of_life_date",
    )
