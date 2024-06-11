from django import forms

class CreateProductoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    cantidad = forms.IntegerField()
    precio = forms.DecimalField(max_digits=10,decimal_places=2)