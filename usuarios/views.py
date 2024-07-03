from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from usuarios.forms import Registro, EditarPerfil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import DatosExtra

def iniciar_sesion(request):
    formulario = AuthenticationForm()
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contrasenia)
            
            login(request, user)
            
            DatosExtra.objects.get_or_create(user=user)
            
            return redirect('inicio')
    return render(request, 'usuarios/iniciar_sesion.html', {'formulario': formulario})

def registro(request):
    formulario =Registro()
    
    if request.method == 'POST':
        formulario = Registro(request.POST)
        if formulario.is_valid():
            formulario.save()
            
            return redirect('login')
        
    return render(request, 'usuarios/registro.html', {'formulario': formulario})

@login_required
def editar_perfil(request):
    formulario = EditarPerfil(initial={'avatar': request.user.datosextra.avatar, 'color_favorito': request.user.datosextra.color_favorito},instance=request.user)
    if request.method == 'POST':
        formulario = EditarPerfil(request.POST,request.FILES ,instance=request.user)
        if formulario.is_valid():
            
            request.user.datosextra.avatar = formulario.cleaned_data.get('avatar')
            request.user.datosextra.color_favorito = formulario.cleaned_data.get('color_favorito')
            request.user.datosextra.save()
            
            formulario.save()
            
            return redirect('editar_perfil')

    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})

class ChangePassword(PasswordChangeView):
    template_name = 'usuarios/cambiar_pass.html'
    success_url = reverse_lazy('editar_perfil')

@login_required
def perfil(request):
    user = request.user
    try:
        datosextra = user.datosextra
    except DatosExtra.DoesNotExist:
        datosextra = None

    contexto = {
        'usuario': user,
        'datosextra': datosextra
    }

    return render(request, 'usuarios/perfil.html', contexto)  
# Create your views here.
