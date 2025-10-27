from django.contrib import admin
from apps.cliente.models import Cliente
# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre","apellido","dni",)
    list_filter = ("nombre","apellido","dni")
    search_fields = ("nombre","apellido","dni","fecha_inscripcion")