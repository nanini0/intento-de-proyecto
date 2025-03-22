from django.shortcuts import render
from .models import Producto
from forms import *


# Create your views here.
def lista_productos(request):
    productos = Producto.objects.all()

    return render(request,'lista_productos.html',{'productos': productos})

def agregar_producto(request):
    return render(request,'agregar_productos.html')

def editar_productos(request):
    return render(request,'editar_productos.html')
