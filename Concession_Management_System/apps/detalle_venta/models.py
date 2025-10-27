from tabnanny import verbose
from django.db import models
from apps.vehiculo.models import Vehiculo

# Create your models here.
class Detalle_venta(models.Model):
    venta = models.ForeignKey('venta.Venta',on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo,on_delete=models.CASCADE)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=3, decimal_places=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "Detalles_ventas"

    def __str__(self):
        return self.id #type: ignore