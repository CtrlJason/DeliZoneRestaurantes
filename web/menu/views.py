from django.shortcuts import render
from firebase import db

# Create your views here.

def menu(request):
    docs = db.collection('restaurante1').document('web').collection('productos').stream()
    contador = 0
    lista_productos = []
    for doc in docs:
        producto_date = doc.to_dict()
        producto_date['id'] = doc.id
        lista_productos.append(producto_date)
        contador+=1
        if contador == 3:
            continue
    # Carrito de compras
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
    return render(request, "menu.html", {
        "lista_productos": lista_productos, 
        "productos_carrito" : productos_carrito, 
        "precio_total" : precio_total,
        "cantidad_productos": cantidad_productos,
        })