from django.urls import path
from .views import (
    VehiculoListView,
    VehiculoCreateView,
    VehiculoUpdateView,
    VehiculoDeleteView,
)

urlpatterns = [
    path('', VehiculoListView.as_view(), name='vehiculo_list'),
    path('nuevo/', VehiculoCreateView.as_view(), name='vehiculo_create'),
    path('<int:pk>/editar/', VehiculoUpdateView.as_view(), name='vehiculo_update'),
    path('<int:pk>/eliminar/', VehiculoDeleteView.as_view(), name='vehiculo_delete'),
]
