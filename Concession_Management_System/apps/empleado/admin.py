# apps/empleado/admin.py
from django.contrib import admin
from .models import Empleado

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    # usa los campos reales que mostró _meta
    list_display = ('id', 'nombre', 'apellido', 'telefono', 'cargo', 'is_staff')
    list_filter = ('cargo', 'is_staff')
    search_fields = ('nombre', 'apellido', 'email', 'telefono')