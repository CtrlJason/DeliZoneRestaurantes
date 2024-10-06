from firebase import db

# class Carrito:
#     def __init__(self, request):
#         self.request = request
#         self.session = request.session
#         carrito = self.session.get("carro")
#         if not carrito:
#             carrito = self.session["carrito"] = {}
#         else:
#             self.carrito = carrito
            
#     def agregar(self, producto):
#         if (str(producto.id) not in self.carrito.keys()):
            
def contenido_carrito():
    docs = db.collection('restaurante1').document('web').collection('carrito').stream()
    
    productos_carrito = []
    precio_total = 0
    cantidad_productos = 0

    for doc in docs:
        productos_data = (doc.to_dict())
        productos_data['id'] = doc.id
        productos_carrito.append(productos_data)
        precio = doc.to_dict()['precio']
        precio_total += precio
        cantidad_productos += 1
        
        datos_carrito = {
            "productos_carrito" : productos_carrito, 
            "precio_total" : precio_total,
            "cantidad_productos": cantidad_productos,
        }
    return datos_carrito