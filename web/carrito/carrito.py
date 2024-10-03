class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carro")
        if not carrito:
            carrito = self.session["carrito"] = {}
        else:
            self.carrito = carrito
            
    def agregar(self, producto):
        if (str(producto.id) not in self.carrito.keys()):
            