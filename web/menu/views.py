from django.shortcuts import render
from productos.productos import Productos

# Create your views here.

def menu(request):
    # Productos de la tienda
    lista_productos = Productos.tienda_productos()
    return render(request, 'menu.html', {'lista_productos': lista_productos})