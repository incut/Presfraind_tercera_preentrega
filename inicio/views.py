from django.shortcuts import render,redirect
from inicio.form import CreateProductoFormulario,BuscarProductoFormulario,EditarProductoFormulario
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
    formulario = BuscarProductoFormulario(request.GET)
    producto = models.Producto.objects.none()
    if formulario.is_valid():
        nombre = formulario.cleaned_data['nombre']
        producto = models.Producto.objects.filter(nombre__icontains=nombre)
    
    return render(request, 'inicio/ver_productos.html', {'producto': producto, 'formulario': formulario})   

def eliminar_producto(request, id):
    producto = models.Producto.objects.get(id=id)
    producto.delete()
    
    return redirect('ver_productos')
    
def editar_producto(request, id):
    producto = models.Producto.objects.get(id=id) 
    
    formulario = EditarProductoFormulario(initial={'nombre': producto.nombre,'precio': producto.precio,'cantidad': producto.cantidad})
    
    if request.method == 'POST':
        formulario = EditarProductoFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            producto.nombre = datos['nombre']
            producto.precio = datos['precio']
            producto.cantidad = datos['cantidad']
            producto.save()
            return redirect('ver_productos')
    return render(request, 'inicio/editar_producto.html', {'formulario': formulario, 'producto': producto})
# Create your views here.
