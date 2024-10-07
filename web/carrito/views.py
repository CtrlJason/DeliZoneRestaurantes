from django.shortcuts import render, redirect
from firebase import db
from .carrito import Carrito

# Create your views here.

def carrito(request):
    origen = str(request.path)
    return render(request, 'ventana_carrito.html', {"origen": origen})

def agregar_producto(request, producto_id, origen):
    producto_ref = db.collection('restaurante1').document('web').collection('productos').document(producto_id).get()
    carrito = Carrito(request)
    if request.method == "POST":
        carrito.agregar(producto_ref)
    return redirect(origen)

def eliminar_producto(request, producto_id, origen):
    producto_ref = db.collection('restaurante1').document('web').collection('productos').document(producto_id).get()
    carrito = Carrito(request)
    if request.method == "POST":
        carrito.eliminar(producto_ref)
    return redirect(origen)
