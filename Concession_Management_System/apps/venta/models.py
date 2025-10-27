from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from apps.cliente.models import Cliente
from apps.empleado.models import Empleado


# --- Funciones para hashear y verificar el número de tarjeta ---
def hash_numero_tarjeta(numero_tarjeta: str) -> str:
    """Hashea el número de tarjeta usando el algoritmo de Django."""
    return make_password(numero_tarjeta)

def verificar_numero_tarjeta(numero_tarjeta: str, numero_hasheado: str) -> bool:
    """Verifica si el número de tarjeta coincide con su hash."""
    return check_password(numero_tarjeta, numero_hasheado)


# --- Modelo de método de pago ---
class Metodo_pago(models.Model):
    nombre = models.CharField(max_length=20)
    debito = models.BooleanField(default=False)
    credito = models.BooleanField(default=False)
    banco = models.CharField(max_length=20, blank=True, null=True)
    numero_tarjeta = models.CharField(max_length=255, blank=True, null=True)
    efectivo = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def guardar(self, *args, **kwargs):
        # Hashea el número de tarjeta si es nuevo o fue modificado
        if self.numero_tarjeta and not self.numero_tarjeta.startswith('pbkdf2_'):
            self.numero_tarjeta = hash_numero_tarjeta(self.numero_tarjeta)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} ({'Efectivo' if self.efectivo else 'Tarjeta'})"


# --- Modelo de venta ---
class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    metodo_pago = models.ForeignKey(Metodo_pago, on_delete=models.CASCADE)
    fecha_venta = models.DateField(auto_now=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "Ventas"

    def __str__(self):
        return f"Venta #{self.id} - Cliente: {self.cliente}" #type: ignore
