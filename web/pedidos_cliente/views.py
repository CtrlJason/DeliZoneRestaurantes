from django.shortcuts import render, redirect
from firebase import db

# Create your views here.

def pedidos_cliente(request):
    if 'clientes_id' not in request.session:
        return redirect('acceder_cliente')
    
    cliente_id = request.session['clientes_id']
    
    # Consultamos los pedidos
    pedidos_ref = db.collection('restaurante1').document('web').collection('pedidos')
    lista_pedidos = []
    try:
        # Hacemos una consulta donde traemos los pedidos con el id de la sesion del cliente y los organizamos de forma descendente por la fecha
        pedidos_query = pedidos_ref.where('cliente_id', '==', cliente_id).order_by('fecha', direction='DESCENDING')
        pedidos = pedidos_query.stream()
        lista_pedidos = [pedido.to_dict() for pedido in pedidos]
    except Exception:
        pedidos = pedidos_ref.where('cliente_id', '==', cliente_id).stream()
        lista_pedidos = [pedido.to_dict() for pedido in pedidos]
    
    return render(request, 'pedidos_cliente.html', {'lista_pedidos': lista_pedidos})