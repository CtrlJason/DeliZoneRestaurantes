from firebase import db

class Productos:
    
    def tienda_productos():
        docs = db.collection('restaurante1').document('web').collection('productos').stream()
        lista_productos = []
        for doc in docs:
            producto_date = doc.to_dict()
            producto_date['id'] = doc.id
            lista_productos.append(producto_date)
        return lista_productos
    
    def tienda_productos_home():
        docs = db.collection('restaurante1').document('web').collection('productos').stream()
        contador = 0
        lista_productos = []
        for doc in docs:
            if contador < 3:
                producto_date = doc.to_dict()
                producto_date['id'] = doc.id
                lista_productos.append(producto_date)
                contador+=1
        return lista_productos