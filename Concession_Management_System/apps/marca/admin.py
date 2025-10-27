from django.contrib import admin
from apps.marca.models import Marca
# Register your models here.
@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ("nombre","razon_social","cuit")
    list_filter = ("nombre","razon_social",)
    search_fields = ("nombre","razon_social",)