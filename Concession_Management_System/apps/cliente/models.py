from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    dni = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15)
    calle = models.CharField(max_length=30)
    numero_calle = models.IntegerField(null=False)
    casa = models.BooleanField()
    edificio = models.BooleanField()
    country_privado = models.BooleanField()
    piso = models.IntegerField(null=True,blank=True)
    numero_casa = models.CharField(max_length=3, null=True, blank=True)

    def __str__(self):
        return self.nombre
