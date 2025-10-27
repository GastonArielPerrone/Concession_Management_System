from django.contrib import admin
from .models import Detalle_venta

@admin.register(Detalle_venta)
class Detalle_ventaAdmin(admin.ModelAdmin):
    # Campos reales del modelo Detalle_venta (según tu salida):
    # ['id', 'venta', 'vehiculo', 'precio_unitario', 'descuento', 'subtotal']
    list_display = ('id', 'venta', 'vehiculo', 'precio_unitario', 'descuento', 'subtotal')
    list_filter = ('vehiculo',)
    search_fields = ('venta__id', 'vehiculo__marca', 'vehiculo__modelo')
