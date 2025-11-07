from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Vehiculo
from .forms import VehiculoForm
from ..marca.models import Marca
from ..modelo.models import Modelo

class VehiculoListView(ListView):
    model = Vehiculo
    template_name = 'vehiculo/vehiculo_list.html'
    context_object_name = 'vehiculos'

    def get_queryset(self):
        queryset = super().get_queryset()
        marca = self.request.GET.get('marca')
        modelo = self.request.GET.get('modelo')
        if marca:
            queryset = queryset.filter(marca__nombre=marca)
        if modelo:
            queryset = queryset.filter(modelo__nombre=modelo)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marcas'] = Marca.objects.all()
        context['modelos'] = Modelo.objects.all()
        return context

class VehiculoCreateView(CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'vehiculo/vehiculo_form.html'
    success_url = reverse_lazy('vehiculo_list')

class VehiculoUpdateView(UpdateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'vehiculo/vehiculo_form.html'
    success_url = reverse_lazy('vehiculo_list')

class VehiculoDeleteView(DeleteView):
    model = Vehiculo
    template_name = 'vehiculo/vehiculo_confirm_delete.html'
    success_url = reverse_lazy('vehiculo_list')