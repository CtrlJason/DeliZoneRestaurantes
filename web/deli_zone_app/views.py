from django.shortcuts import render
from productos.productos import Productos
# from gestion_acceso.acceso import estado_login_usuario

# Create your views here.


def home(request):
    # Productos
    # verificar_login_usuario = estado_login_usuario(request)
    lista_productos = Productos.tienda_productos_home()
    context = {
        "lista_productos": lista_productos,
        }
    return render(request, "home.html", context)
