
from django.urls import path
from . import views  # Importa las vistas

urlpatterns = [
    # Ruta para listar productos
    path('', views.lista_productos, name='lista_productos'),
    path('editar/', views.editar_productos, name='editar_productos'),
]