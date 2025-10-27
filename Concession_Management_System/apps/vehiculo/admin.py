from django.contrib import admin
from apps.vehiculo.models import Vehiculo
# Register your models here.
@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ("modelo","marca")
    list_filter = ("modelo","marca","año","precio_lista")
    search_fields = ("modelo","marca","año","color","numero_chasis","numero_motor","precio_lista",)