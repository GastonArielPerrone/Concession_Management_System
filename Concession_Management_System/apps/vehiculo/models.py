from turtle import color
import turtle
from django.db import models
from apps.marca.models import Marca
from apps.modelo.models import Modelo

# Create your models here.
class Vehiculo(models.Model):
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo,on_delete=models.CASCADE)
    año = models.IntegerField(max_length=4)
    color = models.CharField(max_length=10)
    numero_chasis = models.CharField(max_length=30)
    numero_motor = models.CharField(max_length=30)
    precio_lista = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.marca} - {self.modelo}"
