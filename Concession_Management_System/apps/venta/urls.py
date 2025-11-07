from django.urls import path
from .views import (
    VentaListView,
    VentaCreateView,
)

urlpatterns = [
    path('', VentaListView.as_view(), name='venta_list'),
    path('nueva/', VentaCreateView.as_view(), name='venta_create'),
]
