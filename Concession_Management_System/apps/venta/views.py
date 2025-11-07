from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Venta
from .forms import VentaForm
from ..cliente.models import Cliente
from ..empleado.models import Empleado

class VentaListView(ListView):
    model = Venta
    template_name = 'venta/venta_list.html'
    context_object_name = 'ventas'

    def get_queryset(self):
        queryset = super().get_queryset()
        cliente = self.request.GET.get('cliente')
        empleado = self.request.GET.get('empleado')
        if cliente:
            queryset = queryset.filter(cliente__nombre__icontains=cliente)
        if empleado:
            queryset = queryset.filter(empleado__nombre__icontains=empleado)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientes'] = Cliente.objects.all()
        context['empleados'] = Empleado.objects.all()
        return context

class VentaCreateView(CreateView):
    model = Venta
    form_class = VentaForm
    template_name = 'venta/venta_form.html'
    success_url = reverse_lazy('venta_list')