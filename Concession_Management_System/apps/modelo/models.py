from tabnanny import verbose
from django.db import models
from apps.marca.models import Marca
# Create your models here.
class Modelo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Modelos"

    def __str__(self):
        return self.nombre