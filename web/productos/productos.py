from firebase import db
from datetime import datetime
import pytz

huso_horario = pytz.timezone('America/Bogota')

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
    
    def categorias():
        docs = db.collection('restaurante1').document('web').collection('tienda').document('productos').collection('categorias').get()
        if not docs:
            datos_categoria = {
                "nombre": "categoria 1",
                "productos": {},
                "fecha": datetime.now(huso_horario),}
            db.collection('restaurante1').document('web').collection('tienda').document('productos').collection('categorias').add(datos_categoria)
        docs = db.collection('restaurante1').document('web').collection('tienda').document('productos').collection('categorias').stream()
        lista_categorias = []
        for doc in docs:
            lista_categorias.append(doc.to_dict())
        return lista_categorias