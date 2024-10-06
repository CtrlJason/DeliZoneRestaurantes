from django.shortcuts import render
from firebase import db
from carrito.carrito import contenido_carrito

# Create your views here.

def pasarela_pagos(request):
    carrito_ref = contenido_carrito()
    precio_total =carrito_ref["precio_total"]
    cantidad_productos =carrito_ref["cantidad_productos"]
    productos_carrito = carrito_ref["productos_carrito"]
    return render(request, "realizar_pago.html", {
        "precio_total" : precio_total,
        "cantidad_productos" : cantidad_productos,
        "productos_carrito" : productos_carrito,
        })
    
def seleccionar_tienda(request):
    carrito_ref = contenido_carrito()
    cantidad_productos =carrito_ref["cantidad_productos"]
    return render(request, "seleccionar_tienda.html", {
        "cantidad_productos" : cantidad_productos,
        })