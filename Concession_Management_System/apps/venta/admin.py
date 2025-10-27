# apps/venta/admin.py
from django.contrib import admin
from .models import Venta

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    # según tu salida de fields: ['detalle_venta', 'id', 'cliente', 'empleado', 'metodo_pago', 'fecha_venta', 'total']
    list_display = ('id', 'cliente', 'empleado', 'metodo_pago', 'fecha_venta', 'total')
    list_filter = ('metodo_pago', 'fecha_venta')
    search_fields = ('cliente__nombre', 'cliente__apellido', 'empleado__nombre', 'empleado__apellido')

    def marca(self, obj):
        # evita AttributeError si vehiculo puede ser None
        return obj.vehiculo.marca if obj.vehiculo else None
    marca.short_description = 'Marca'
    # para poder ordenar por la marca del vehiculo (si tu DB lo permite):
    marca.admin_order_field = 'vehiculo__marca'

    def modelo(self, obj):
        return obj.vehiculo.modelo if obj.vehiculo else None
    modelo.short_description = 'Modelo'
    modelo.admin_order_field = 'vehiculo__modelo'