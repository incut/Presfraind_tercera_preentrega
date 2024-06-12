from django import forms

class ProductoFormularioBase(forms.Form):
    nombre = forms.CharField(max_length=30)
    cantidad = forms.IntegerField()
    precio = forms.DecimalField(max_digits=10,decimal_places=2)
    
class CreateProductoFormulario(ProductoFormularioBase):
    ...
class EditarProductoFormulario(ProductoFormularioBase):
    ...
    
class BuscarProductoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)