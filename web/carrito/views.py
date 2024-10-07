from django.shortcuts import render, redirect
from firebase import db
from .carrito import Carrito

# Create your views here.

def carrito(request):
    return render(request, 'ventana_carrito.html')

def agregar_producto(request, producto_id, origen):
    producto_ref = db.collection('restaurante1').document('web').collection('productos').document(producto_id).get()
    print(producto_ref)
    carrito = Carrito(request)
    if request.method == "POST":
        carrito.agregar(producto_ref)
    return redirect(origen)
