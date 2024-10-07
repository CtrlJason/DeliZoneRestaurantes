from django.shortcuts import render
from productos.productos import Productos
from gestion_acceso.acceso import estado_login

# Create your views here.

def menu(request):
    # Productos de la tienda
    lista_productos = Productos.tienda_productos()
    login = estado_login(request)
    context = {
        'lista_productos': lista_productos,'login': login
    }
    return render(request, 'menu.html', context)