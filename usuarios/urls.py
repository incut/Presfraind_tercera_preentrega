from django.urls import path
from django.contrib.auth.views import LogoutView
from usuarios import views
urlpatterns = [
    path('logout/', LogoutView.as_view(template_name='usuarios/cerrar_sesion.html'), name='logout'),
    path('login/', views.iniciar_sesion , name='login'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/editar/password/', views.ChangePassword.as_view(), name='cambiar_pass'),
]
