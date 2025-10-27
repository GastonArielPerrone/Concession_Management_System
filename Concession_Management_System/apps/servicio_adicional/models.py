from tabnanny import verbose
from django.db import models

# Create your models here.
class Servicio_adicional(models.Model):
    venta = models.ForeignKey('venta.Venta', on_delete=models.CASCADE)
    nombre_servicio = models.CharField(max_length=20)
    precio_servicio = models.DecimalField(max_digits=9, decimal_places=2)
    descripcion = models.TextField(max_length=6000)

    class Meta:
        verbose_name_plural = "Servicios"

    def __str__(self):
        return self.nombre_servicio