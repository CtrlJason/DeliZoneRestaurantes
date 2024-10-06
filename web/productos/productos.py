from firebase import db

def tienda_productos():
    docs = db.collection('restaurante1').document('web').collection('productos').stream()
    lista_productos = []
    for doc in docs:
        producto_date = doc.to_dict()
        producto_date['id'] = doc.id
        lista_productos.append(producto_date)
    return lista_productos