from django.shortcuts import render, redirect
from gestion_acceso.acceso import estado_login

# Create your views here.

def pasarela_pagos(request):
    login = estado_login()
    if 'clientes_id' not in request.session:
        return redirect('acceder_cliente')
    else:
        return render(request, "realizar_pago.html", {
            "login": login
            })
    
def seleccionar_tienda(request):
    login = estado_login()
    if 'clientes_id' not in request.session:
        return redirect('acceder_cliente')
    else:
        return render(request, "seleccionar_tienda.html", { "login": login })