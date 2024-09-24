from django.shortcuts import render, redirect
from .forms import ProductoForm
from firebase import db

# Create your views here.

def formatear_precio(precio):
        return

def eliminar_producto(request, producto_id):
    return redirect('productos')

def productos(request):
    return render(request, 'productos.html', {'productos': productos}) # Enviamos los productos al template 'productos'
