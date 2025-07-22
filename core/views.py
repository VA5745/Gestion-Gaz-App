from datetime import date

from django.views.generic import TemplateView
from equipment.models import Device
from maintenance.models import MaintenanceRecord


class DashboardView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["device_count"] = Device.objects.count()
        context["maintenance_count"] = MaintenanceRecord.objects.count()
        context["obsolete_count"] = Device.objects.filter(end_of_life_date__lt=date.today()).count()
        return context
