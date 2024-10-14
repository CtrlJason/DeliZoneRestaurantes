from django.shortcuts import render, redirect

# Create your views here.

def pasarela_pagos(request):
    if 'clientes_id' not in request.session:
        return redirect('acceder_cliente')
    else:
        
        return render(request, "realizar_pago.html", {
            })
    
def seleccionar_tienda(request):
    if 'clientes_id' not in request.session:
        return redirect('acceder_cliente')
    else:
        return render(request, "seleccionar_tienda.html")