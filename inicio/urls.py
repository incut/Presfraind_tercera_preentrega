from django.urls import path
from inicio import views
urlpatterns = [
   path('', views.inico, name= 'inicio'),
   path('producto/', views.ver_productos, name= 'ver_productos'),
   path('producto/crear/', views.agregar_producto, name= 'agregar_producto'),
   path('producto/eliminar/<int:id>', views.eliminar_producto, name= 'eliminar_producto'),
   path('producto/editar/<int:id>', views.editar_producto, name= 'editar_producto'),
]
