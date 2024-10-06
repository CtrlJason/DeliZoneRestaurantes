from django.shortcuts import render
from carrito.carrito import contenido_carrito
from productos.productos import tienda_productos

# Create your views here.

def menu(request):
    # Productos de la tienda
    lista_productos = tienda_productos()
    # Carrito de compras
    carrito_ref = contenido_carrito()
    cantidad_productos = carrito_ref["cantidad_productos"]
    productos_carrito = carrito_ref["productos_carrito"]
    return render(request, "menu.html", {"lista_productos": lista_productos, "cantidad_productos": cantidad_productos, "productos_carrito": productos_carrito})