from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    cantidad = models.IntegerField(default=0)
    precio = models.DecimalField(default=0,max_digits=10,decimal_places=2)
        
    def __str__(self):
        return f'Nombre: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}'
# Create your models here.
