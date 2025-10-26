from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=10)
    razon_social = models.CharField(max_length=20)
    cuit = models.CharField(max_length=15)
    telefono = models.CharField(max_length=15)
    calle = models.CharField(max_length=20)
    numero_calle = models.IntegerField()

    def __str__(self):
        return self.nombre