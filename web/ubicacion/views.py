from django.shortcuts import render
from firebase import db

# Create your views here.

def ubicacion(request):
    # Contador del carrito de compras
    docs_car = db.collection('carrito').stream()
    cantidad_productos = 0

    for i in docs_car:
        cantidad_productos += 1
    return render(request, "ubicacion.html", {"cantidad_productos" : cantidad_productos})