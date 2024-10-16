from django.shortcuts import render, redirect
from firebase import db
from carrito.carrito import Carrito
from datetime import datetime
import pytz

huso_horario = pytz.timezone('America/Bogota')

# Create your views here.

def pasarela_pagos(request):
    if 'clientes_id' not in request.session:
        return redirect('acceder_cliente')
    else:
        return render(request, "pasarela_pagos.html", {
            })
    
def seleccionar_tienda(request):
    if 'clientes_id' not in request.session:
        return redirect('acceder_cliente')
    else:
        return render(request, "seleccionar_tienda.html")
    
def realizar_pago(request):
    if request.method == 'POST':
        carrito = Carrito(request)
        
        cliente_id = request.session['clientes_id']
        cliente_ref = db.collection('restaurante1').document('usuarios').collection('clientes').document(cliente_id)
        cliente = cliente_ref.get()
        
        datos_pedido = {
            'cliente_id': cliente_id,
            'nombre_cliente': cliente.to_dict().get('nombres') + ' ' + cliente.to_dict().get('apellidos'),
            'correo_cliente': cliente.to_dict().get('correo'),
            'celular_cliente': cliente.to_dict().get('celular'),
            'direccion': cliente.to_dict().get('direccion'),
            'productos': [],
            'total': carrito.carrito['precio_total'],
            'fecha': datetime.now(huso_horario),
            'estado': 'pendiente',
        }
        print(datos_pedido)
        
        # Restamos el stock de los productos
        for producto_id, item in carrito.carrito['productos'].items():
            producto_ref = db.collection('restaurante1').document('web').collection('productos').document(producto_id)
            producto = producto_ref.get()
            if producto.exists:
                producto_data = producto.to_dict()
                stock = producto_data.get('stock', 0)
                nuevo_stock = (stock - item['cantidad'])
                
                # Actualizamos el stock
                producto_ref.update({'stock': nuevo_stock})
                
                # Añadimos el producto al pedido
                datos_pedido['productos'].append({
                    'producto_id': producto_id,
                    'nombre_pedido': item['nombre'],
                    'cantidad': item['cantidad'],
                    'precio_unidad': item['precio_unidad'],
                    'imagen' : producto_data.get('imagen'),
                })
        # Guardamos el pedido en Firebase
        db.collection('restaurante1').document('web').collection('pedidos').add(datos_pedido)
        
        # Limpiamos el carrito
        if 'clientes_id' in request.session:
            cliente_id = request.session['clientes_id']
            request.session[f'carrito_cliente_{cliente_id}'] = {
                'productos': {},
                'cantidad_total': 0,
                'precio_total': 0,
            }
        else:
            request.session['carrito'] = {
                'productos': {},
                'cantidad_total': 0,
                'precio_total': 0,
            }
            
        request.session.modified = True
        return redirect('home')
    else: 
        return redirect('pasarela_pagos')

def enviar_direccion(request):
    if request.method == 'POST':
        
        cliente_id = request.session['clientes_id']
        cliente_ref = db.collection('restaurante1').document('usuarios').collection('clientes').document(cliente_id)
        cliente_ref.update({
            'direccion': {
                'Ciudad': request.POST.get('Ciudad'),
                'localidad': request.POST.get('localidad'),
                'barrio': request.POST.get('barrio'),
                'Direccion': request.POST.get('Direccion'),
                'datos': {
                    request.POST.get('dato-1'),
                    request.POST.get('dato-2'),
                    request.POST.get('dato-3'),
                        },
                'codigo_postal': request.POST.get('codigo_postal'),
                'referencia': request.POST.get('referencia')
            }
        })
        return redirect('pasarela_pagos')