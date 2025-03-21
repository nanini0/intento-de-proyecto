from django.shortcuts import render
from .models import Producto



# Create your views here.
def lista_productos(request):
    productos = Producto.objects.all()

    return render(request,'lista_productos.html',{'productos': productos})

def editar_productos(request):
    return render(request,'editar_productos.html')
