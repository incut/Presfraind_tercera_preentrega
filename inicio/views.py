from typing import Any
from django.shortcuts import render
from inicio.form import BuscarProductoFormulario,EditarProductoFormulario
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from inicio.models import Producto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


def inico (request):
    return render(request, 'inicio/inicio.html')

class Productos(LoginRequiredMixin, ListView):
    model = Producto 
    template_name = 'inicio/ver_productos.html'
    context_object_name = 'productos'
    paginate_by = 10
    
    def get_queryset(self):
        nombre = self.request.GET.get('nombre', '')
        if nombre:
            return self.model.objects.filter(nombre__icontains=nombre)
        else:
            return self.model.objects.all()
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formulario'] = BuscarProductoFormulario()
        context['nombre'] = self.request.GET.get('nombre', '')
        return context

class CrearProducto(LoginRequiredMixin,CreateView):
    model = Producto
    template_name = 'inicio/crear_producto.html'
    success_url = reverse_lazy('ver_productos')
    fields = ['nombre','marca' ,'cantidad', 'precio', 'fecha', 'foto']

class EliminarProducto(LoginRequiredMixin,DeleteView):
    model = Producto
    template_name = "inicio/eliminar_producto.html"
    success_url = reverse_lazy('ver_productos')
    
class EditarProducto(LoginRequiredMixin,UpdateView):
    model = Producto
    template_name = "inicio/editar_producto.html"
    success_url = reverse_lazy('ver_productos')
    fields = ['nombre','marca' ,'cantidad', 'precio', 'fecha','foto']

class VerProductos(DetailView):
    model = Producto
    template_name = "inicio/producto.html"
    context_object_name = 'producto'

def about(request):
    return render(request, 'inicio/sobre_mi.html')





