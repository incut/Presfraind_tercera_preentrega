from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User

class Registro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasenia', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contrasenia', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        helps_text = {key: '' for key in fields}
        
class EditarPerfil(UserChangeForm):
    password = None
    email = forms.EmailField()
    first_name = forms.CharField(label='nombre')
    last_name = forms.CharField(label='apellido')
    avatar = forms.ImageField(required=False) 
    color_favorito = forms.CharField(label='color favorito')
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'avatar','color_favorito'] 
    
