from django.shortcuts import render
from firebase import db

# Create your views here.

def pasarela_pagos(request):
    docs_car = db.collection('carrito').stream()
    productos_carrito = []
    
    precio_total = 0
    cantidad_productos = 0
    
    for doc in docs_car:
        productos_data = (doc.to_dict())
        productos_data['id'] = doc.id
        productos_carrito.append(productos_data)
        precio = doc.to_dict()['precio']
        precio_total += precio
        cantidad_productos += 1
    return render(request, "realizar_pago.html", {
        "precio_total" : precio_total,
        "cantidad_productos" : cantidad_productos,
        "productos_carrito" : productos_carrito,
        })
    
def escoger_tienda(request):
    docs_car = db.collection('carrito').stream()
    cantidad_productos = 0
    
    for doc in docs_car:
        cantidad_productos += 1
    return render(request, "escoger_tienda.html", {
        "cantidad_productos" : cantidad_productos,
        })