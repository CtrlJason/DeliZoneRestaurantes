from django.shortcuts import render
from gestion_acceso.acceso import estado_login

# Create your views here.

def ubicacion(request):
    # Contador del carrito de compras
    login = estado_login(request)
    return render(request, "ubicacion.html", { "login": login })