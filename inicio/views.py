from django.shortcuts import render,redirect
from inicio.form import CreateProductoFormulario
from inicio import models

def inico (request):
    return render(request, 'inicio/inicio.html')

def agregar_producto(request):
    formulario = CreateProductoFormulario()
    
    if request.method == 'POST':
        formulario = CreateProductoFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            producto = models.Producto(
                nombre=datos['nombre'],
                cantidad=datos['cantidad'],
                precio=datos['precio']
            )
            producto.save()
            return redirect('ver_productos')
                   
    return render(request, 'inicio/crear_producto.html', {'formulario': formulario }) 

def ver_productos(request):
    
    productos = models.Producto.objects.all()
    
    return render(request, 'inicio/ver_productos.html', {'producto': productos})   
    
# Create your views here.
