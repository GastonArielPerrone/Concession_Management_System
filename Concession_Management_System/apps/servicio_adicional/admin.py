from django.contrib import admin
from apps.servicio_adicional.models import Servicio_adicional
# Register your models here.
@admin.register(Servicio_adicional)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ("nombre_servicio", "venta")
    list_filter = ("nombre_servicio", "venta","precio_servicio")
    search_fields = ("nombre_servicio", "venta","precio_servicio",)