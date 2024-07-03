from django.db import models
from datetime import date

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(default='proyecto',max_length=20)
    cantidad = models.IntegerField(default=0)
    precio = models.DecimalField(default=0,max_digits=10,decimal_places=2)
    foto = models.ImageField(upload_to='fotos', blank=True, null=True)
    fecha = models.DateField(default = date.today )
        
    def __str__(self):
        return f'Nombre: {self.nombre},Marca: {self.marca}, Precio: {self.precio}, Cantidad: {self.cantidad}, año: {self.fecha}'
# Create your models here.
