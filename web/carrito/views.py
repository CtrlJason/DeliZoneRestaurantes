from django.shortcuts import render, redirect
from firebase import db
from .carrito import contenido_carrito

# Create your views here.

def carrito(request):
    carrito_ref = contenido_carrito()
    productos_carrito = carrito_ref["productos_carrito"]
    return render(request, 'ventana_carrito.html', { "productos_carrito" : productos_carrito })

def agregar_producto(request, producto_id):
    producto_ref = db.collection('restaurante1').document('web').collection('productos').document(producto_id).get()
    producto = producto_ref.to_dict()
    if request.method == "POST":
        db.collection('restaurante1').document('web').collection('carrito').add({
            'nombre' : producto["nombre"],
            'precio' : producto["precio"],
            'imagen' : producto["imagen"],
        })
    return redirect('home')
