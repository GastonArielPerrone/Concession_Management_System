from django.db import models
from apps.cliente.models import Cliente
from apps.empleado.models import Empleado # type: ignore

# Create your models here.
class Metodo_pago(models.Model):
    nombre = models.CharField(max_length=20)
    debito = models.BooleanField()
    credito = models.BooleanField()
    efectivo = models.BooleanField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre
class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, null=False, on_delete=models.CASCADE)
    fecha_venta = models.DateField(auto_now=True)
    metodo_pago = models.ForeignKey(Metodo_pago, null=False, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2,)

    def __str__(self):
        return self.cliente
