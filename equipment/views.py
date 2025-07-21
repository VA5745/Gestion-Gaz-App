from django.views.generic import ListView
from .models import Device


class DeviceListView(ListView):
    model = Device
    template_name = "device_list.html"
