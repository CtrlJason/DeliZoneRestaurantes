from django.shortcuts import render
from firebase_admin import firestore

# Create your views here.

# Instancia de Firestore
db = firestore.client()

def home(request):
    productos_ref = db.collection('productos')
    docs = productos_ref.stream()

    productos = [doc.to_dict() for doc in docs]
    
    # Asegúrate de que hay suficientes productos
    producto1 = productos[0]
    producto2 = productos[1]
    producto3 = productos[2]

    context = {
        'producto1': producto1,
        'producto2': producto2,
        'producto3': producto3,
    }
    
    def formatear_precio(precio):
        return f"${precio:,.2f}"

    if producto1:
        producto1['precio_formateado'] = formatear_precio(producto1.get('precio', 0))
    if producto2:
        producto2['precio_formateado'] = formatear_precio(producto2.get('precio', 0))
    if producto3:
        producto3['precio_formateado'] = formatear_precio(producto3.get('precio', 0))

    context = {
        'producto1': producto1,
        'producto2': producto2,
        'producto3': producto3,
    }
    
    return render(request, 'home.html', context)