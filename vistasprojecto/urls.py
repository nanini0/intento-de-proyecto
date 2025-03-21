
from django.urls import path
from . import views  # Importa las vistas

urlpatterns = [
    # Ruta para listar productos
    path('', views.lista_productos, name='lista_productos'), 
    path('agregar_productos/', views.agregar_producto, name='agregar_productos'),
    path('editar/', views.editar_productos, name='editar_productos'),
]