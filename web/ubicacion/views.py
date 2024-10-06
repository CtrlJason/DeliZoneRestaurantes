from django.shortcuts import render
from firebase import db
from carrito.carrito import contenido_carrito

# Create your views here.

def ubicacion(request):
    # Contador del carrito de compras
    carrito_ref = contenido_carrito()
    cantidad_productos = carrito_ref["cantidad_productos"]
    productos_carrito = carrito_ref["productos_carrito"]
    return render(request, "ubicacion.html", {"cantidad_productos" : cantidad_productos, "productos_carrito": productos_carrito})