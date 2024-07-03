from django.db import models
from django.contrib.auth.models import User

class DatosExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', blank=True, null=True)
    color_favorito= models.CharField(default='no tengo',max_length=20)

# Create your models here.
