from firebase import db

# imagen
def imagen_admin(request):
    imagen_administrador = "https://firebasestorage.googleapis.com/v0/b/delizone-1a227.appspot.com/o/DeliZone%2FCliente%2Fuser-circle.svg?alt=media&token=441d982f-9a62-4ea4-a144-2681814b11e7"
    if 'administradores_id' not in request.session:
        return {"imagen_administrador": imagen_administrador}
    else:
        admin_id = request.session['administradores_id']
        docs = db.collection('restaurante1').document('usuarios').collection('administradores').stream()
        try: 
            for doc in docs:
                usuarios_data = (doc.to_dict())
                if doc.id == admin_id:
                    imagen_administrador = usuarios_data['imagen']
            return {"imagen_administrador": imagen_administrador}
        except Exception as e:
            print(e)
            return {"imagen_administrador": imagen_administrador}

def imagen_cliente(request):
    imagen_clientes = "https://firebasestorage.googleapis.com/v0/b/delizone-1a227.appspot.com/o/DeliZone%2FCliente%2Fuser-circle-black.svg?alt=media&token=667e6bbd-7acb-4655-b5cb-697347ef3883"
    if 'clientes_id' not in request.session:
        return {"imagen_clientes": imagen_clientes}
    else:
        cliente_id = request.session['clientes_id']
        docs = db.collection('restaurante1').document('usuarios').collection('clientes').stream()
        try: 
            for doc in docs:
                usuarios_data = (doc.to_dict())
                if doc.id == cliente_id:
                    imagen_clientes= usuarios_data['imagen']
            return {"imagen_clientes": imagen_clientes}
        except Exception as e:
            print(f"La imagen no existe o no se cargo correctamente{e}")
            return {"imagen_clientes": imagen_clientes}