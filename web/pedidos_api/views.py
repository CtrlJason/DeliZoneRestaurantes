from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from firebase import db
from carrito.carrito import Carrito
from datetime import datetime
import pytz

# Guardamos el uso horario de la ubicación actaul de donde se almacena el proyecto
uso_horario = pytz.timezone('America/Bogota')

class PedidoApiView(APIView):
    # Ver todos los pedidos
    def get(self, request):
        try:
            # Consultamos los pedidos
            pedidos_ref = db.collection('restaurante1').document('web').collection('pedidos')
            lista_pedidos = []
            try:
                pedidos = pedidos_ref.stream()
                lista_pedidos = [pedido.to_dict() for pedido in pedidos]
            except Exception:
                pedidos = pedidos_ref.stream()
                lista_pedidos = [pedido.to_dict() for pedido in pedidos]
            return Response(lista_pedidos, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self, request):
        if request.method == 'POST':
            try:
                carrito = Carrito(request)
                
                # Guardamos el id del usuario para usarlo posteriormente
                cliente_id = request.session['clientes_id']
                cliente_ref = db.collection('restaurante1').document('usuarios').collection('clientes').document(cliente_id)
                cliente = cliente_ref.get()
                
                # Creamos el pedido
                datos_pedido = {
                    'cliente_id': cliente_id,
                    'nombre_cliente': cliente.to_dict().get('nombres') + ' ' + cliente.to_dict().get('apellidos'),
                    'correo_cliente': cliente.to_dict().get('correo'),
                    'celular_cliente': cliente.to_dict().get('celular'),
                    'direccion': cliente.to_dict().get('direccion'),
                    'productos': [],
                    'total': carrito.carrito['precio_total'],
                    'fecha': datetime.now(uso_horario),
                    'estado': 'pendiente',
                }
                
                for producto_id, item in carrito.carrito['productos'].items():
                    producto_ref = db.collection('restaurante1').document('web').collection('productos').document(producto_id)
                    producto = producto_ref.get()
                    
                    if producto.exists:
                        # Restamos el stock de los productos
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
                        
                        # Guardamos el pedido en FireBase
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
                        
                        return Response({'message': 'Pedido creado exitosamente'}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return redirect('pasarela_pagos')

# Create your views here.

# @api_view(['GET'])
# def ver_pedidos(request):
#     try:
#         # Consultamos los pedidos
#         pedidos_ref = db.collection('restaurante1').document('web').collection('pedidos')
#         lista_pedidos = []
#         try:
#             pedidos = pedidos_ref.stream()
#             lista_pedidos = [pedido.to_dict() for pedido in pedidos]
#         except Exception:
#             pedidos = pedidos_ref.stream()
#             lista_pedidos = [pedido.to_dict() for pedido in pedidos]
#         return Response(lista_pedidos, status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# @api_view(['POST'])
# def crear_pedido(request):
#     if request.method == 'POST':
#         try:
#             carrito = Carrito(request)
            
#             # Guardamos el id del usuario para usarlo posteriormente
#             cliente_id = request.session['clientes_id']
#             cliente_ref = db.collection('restaurante1').document('usuarios').collection('clientes').document(cliente_id)
#             cliente = cliente_ref.get()
            
#             # Creamos el pedido
#             datos_pedido = {
#                 'cliente_id': cliente_id,
#                 'nombre_cliente': cliente.to_dict().get('nombres') + ' ' + cliente.to_dict().get('apellidos'),
#                 'correo_cliente': cliente.to_dict().get('correo'),
#                 'celular_cliente': cliente.to_dict().get('celular'),
#                 'direccion': cliente.to_dict().get('direccion'),
#                 'productos': [],
#                 'total': carrito.carrito['precio_total'],
#                 'fecha': datetime.now(uso_horario),
#                 'estado': 'pendiente',
#             }
            
#             for producto_id, item in carrito.carrito['productos'].items():
#                 producto_ref = db.collection('restaurante1').document('web').collection('productos').document(producto_id)
#                 producto = producto_ref.get()
                
#                 if producto.exists:
#                     # Restamos el stock de los productos
#                     producto_data = producto.to_dict()
#                     stock = producto_data.get('stock', 0)
#                     nuevo_stock = (stock - item['cantidad'])
                    
#                     # Actualizamos el stock
#                     producto_ref.update({'stock': nuevo_stock})
                    
#                     # Añadimos el producto al pedido
#                     datos_pedido['productos'].append({
#                         'producto_id': producto_id,
#                         'nombre_pedido': item['nombre'],
#                         'cantidad': item['cantidad'],
#                         'precio_unidad': item['precio_unidad'],
#                         'imagen' : producto_data.get('imagen'),
#                     })
                    
#                     # Guardamos el pedido en FireBase
#                     db.collection('restaurante1').document('web').collection('pedidos').add(datos_pedido)
                    
#                     # Limpiamos el carrito
#                     if 'clientes_id' in request.session:
#                         cliente_id = request.session['clientes_id']
#                         request.session[f'carrito_cliente_{cliente_id}'] = {
#                             'productos': {},
#                             'cantidad_total': 0,
#                             'precio_total': 0,
#                         }
#                     else:
#                         request.session['carrito'] = {
#                             'productos': {},
#                             'cantidad_total': 0,
#                             'precio_total': 0,
#                         }
#                     request.session.modified = True
                    
#                     return redirect('home')
#         except Exception as e:
#             return Response({
#                 'error': str(e)
#             }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#     else:
#         return redirect('pasarela_pagos')
    
