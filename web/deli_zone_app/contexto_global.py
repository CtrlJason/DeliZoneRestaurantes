from firebase import db

# Exclusion de urls
def excluir_paths_sitio(request):
    excluir_paths = [
        "/acceso/iniciar_sesion/",
        "/acceso/iniciar_sesion_admin/",
        "/acceso/registro/",
        "/carrito/",
        "/compra/",
        "/seleccionar_tienda/pasarela_pagos/",
        "/acceso/",
        "/seleccionar_tienda/",
        "/dashboard/",
        "/dashboard/admin/",
        "/dashboard/admin/productos/",
        "/dashboard/admin/contacto/",
        "/dashboard/admin/configuracion/sitio/",
        "/dashboard/admin/usuarios/",
        "/configuracion/admin/",
        "/dashboard/admin/configuracion/sitio/sitio/",
    ]
    return {"excluir_paths": excluir_paths}

# Imagenes del sitio

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
                    imagen_clientes = usuarios_data['imagen']
            return {"imagen_clientes": imagen_clientes}
        except Exception as e:
            print(f"La imagen no existe o no se cargo correctamente{e}")
            return {"imagen_clientes": imagen_clientes}
        
# Configuracion del sitio

def fav_icon_sitio(request):
    config_doc = db.collection('restaurante1').document('configuracion').get()
    if config_doc.exists:
        fav_icon = config_doc.get('fav_icon_sitio')
        return {"fav_icon_sitio": fav_icon}
    else:
        fav_icon = 'https://firebasestorage.googleapis.com/v0/b/delizone-1a227.appspot.com/o/restaurante1%2Fimagenes%2FLogo.svg?alt=media&token=24af3c22-2bb4-4538-ae2c-59b339e23efd'
        return {"fav_icon_sitio": fav_icon}

def logo_sitio(request):
    config_doc = db.collection('restaurante1').document('configuracion').get()
    if config_doc.exists:
        logo = config_doc.get('logo')
        return {"logo_sitio": logo}
    else:
        logo = 'https://firebasestorage.googleapis.com/v0/b/delizone-1a227.appspot.com/o/restaurante1%2Fimagenes%2FLocoConTexto.svg?alt=media&token=7a5b0bc9-7360-4d12-815f-cf60031a0ced'
        return {"logo_sitio": logo}

def colores_sitio(request):
    config_doc = db.collection('restaurante1').document('configuracion').get()
    if config_doc.exists:
        context = {
            'color1': config_doc.get('color1'),
            'color2': config_doc.get('color2'),
            'color3': config_doc.get('color3'),
            'colorbordeboton': config_doc.get('colorbordeboton'),
            'colorboton1': config_doc.get('colorboton1'),
            'colorboton2': config_doc.get('colorboton2'),
        }
        return context
    else:
        context = {
            'color1': '#fff',
            'color2': '#042434',
            'color3': '#161A1D',
            'colorbordeboton': '#660708',
            'colorboton1': '#E5383B',
            'colorboton2': '#BA181B',
        }
        return context