class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        
        # Verificamos si el usuario esta logeado
        if 'clientes_id' in request.session:
            cliente_id = request.session['clientes_id']
            carrito = self.session.get(f'carrito_cliente_{cliente_id}')
        else:
            # Si el usuario no ha iniciado sesion, utiliza un carrito temporal
            carrito = self.session.get('carrito')
            
        # Si no existe un carrito para el usuario, lo inicializamos
        if not carrito:
            carrito = self.session[f'carrito_cliente_{cliente_id}' if 'clientes_id' in request.session else 'carrito'] = {
                'productos': {},
                'cantidad_total': 0,
                'precio_total': 0,
            }
        self.carrito = carrito
    
    def agregar(self, producto_ref):
        # Contenido del producto
        producto = producto_ref.to_dict()
        
        # Si el producto no está en el carrito, lo agregamos
        if producto_ref.id not in self.carrito['productos'].keys():
            self.carrito['productos'][producto_ref.id] = {
                'producto_id' : producto_ref.id,
                'nombre': producto['nombre'],
                'imagen': producto['imagen'],
                'precio_unidad': producto['precio'],
                'cantidad': 1,
            }
            # Aumentamos la cantidad total y el precio total del carrito
            self.carrito['cantidad_total'] += 1
            self.carrito['precio_total'] += producto['precio']
        else:
            # Si el producto ya existe en el carrito, aumentamos la cantidad y el precio total
            self.carrito['productos'][producto_ref.id]['cantidad'] += 1
            self.carrito['cantidad_total'] += 1
            self.carrito['precio_total'] += producto['precio']
        self.guardar_carrito() # Guardar el carrito actualizado en la sesión

    def eliminar(self, producto_ref):
        try:
            # Verificar si el producto está en el carrito
            if producto_ref.id in self.carrito['productos']:
                producto = self.carrito['productos'][producto_ref.id]
                
                # Actualizamos la cantidad total y el precio total
                self.carrito['cantidad_total'] -= 1
                self.carrito['precio_total'] -= producto['precio_unidad']
                
                if producto['cantidad'] > 1:
                    # Reducimos la cantidad de del producto en caso de que haya mas de 1
                    producto['cantidad'] -= 1
                    # Actualizamos el precio total restando el precio del producto
                    # self.carrito['precio_total'] -= producto['precio']
                    
                else:
                    del self.carrito['productos'][producto_ref.id]
                    
                self.guardar_carrito() # Guardamos el carrito actualizado en la sesión
        except Exception as e:
            print(f"Error al eliminar producto: {e}")
            
    def guardar_carrito(self):
        self.session['carrito'] = self.carrito
        self.session.modified = True #Al marcar la sesión como modificada, se asegura que Django guarde los cambios en la sesión.

def datos_carrito(request):
    # Crear una instancia del carrito con la request actual
    carrito = Carrito(request)
    # Esto comprueba si existen productos, si no existen envia el diccionario vacio
    productos_carrito = carrito.carrito.get('productos', {})
    # Cantidad total de productos y el precio total
    cantidad_total = carrito.carrito.get('cantidad_total', 0)
    precio_total = carrito.carrito.get('precio_total', 0)
    return {
        "productos_carrito": productos_carrito,
        "cantidad_total": cantidad_total,
        "precio_total": precio_total
        }