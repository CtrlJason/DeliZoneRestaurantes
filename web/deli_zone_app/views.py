from django.shortcuts import render
from productos.productos import Productos
from gestion_acceso.acceso import estado_login

# Create your views here.


def home(request):
    # Productos
    lista_productos = Productos.tienda_productos_home()
    login = estado_login(request)
    context = {"lista_productos": lista_productos, "login": login}
    return render(request, "home.html", context)
