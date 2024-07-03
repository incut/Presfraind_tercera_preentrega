from django.urls import path
from inicio import views
urlpatterns = [
   path('', views.inico, name= 'inicio'),
   path('about/',views.about, name='about' ),
   path('producto/', views.Productos.as_view(), name='ver_productos'),
   path('producto/agregar/', views.CrearProducto.as_view(), name='agregar_producto'),
   path('producto/<int:pk>/', views.VerProductos.as_view(), name='detalle_productos'),
   path('producto/eliminar/<int:pk>/', views.EliminarProducto.as_view(), name='eliminar_producto'),
   path('producto/editar/<int:pk>/', views.EditarProducto.as_view(), name='editar_producto'),

]
