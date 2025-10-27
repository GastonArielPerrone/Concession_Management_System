from ast import Mod
from django.contrib import admin
from apps.modelo.models import Modelo
# Register your models here.
@admin.register(Modelo)
class ModeloAdmin(admin.ModelAdmin):
    list_display = ("nombre","marca",)
    list_filter = ("nombre","marca",)
    search_fields = ("nombre","marca","descripcion",)