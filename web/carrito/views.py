from django.shortcuts import render, redirect
from firebase import db

# Create your views here.

def carrito(request):
    docs = db.collection('carrito').stream()
    productos_carrito = []
    precio_total = 0
    for doc in docs:
        productos_data = (doc.to_dict())
        productos_data['id'] = doc.id
        productos_carrito.append(productos_data)
        precio = doc.to_dict()['precio']
        precio_total += precio
    return render(request, 'ventana_carrito.html', { "productos_carrito" : productos_carrito })

def agregar_producto(request, producto_id):
    producto_ref = db.collection('productos').document(producto_id).get()
    producto = producto_ref.to_dict()
    if request.method == "POST":
        db.collection('carrito').add({
            'nombre' : producto["nombre"],
            'precio' : producto["precio"],
            'imagen' : producto["imagen"],
        })
    return redirect('home')
