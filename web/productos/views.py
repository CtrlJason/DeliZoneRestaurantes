from django.shortcuts import render, redirect
from .forms import ProductoForm
from firebase_admin import firestore, storage

# Instancia de Firestore y Storage
db = firestore.client()
bucket = storage.bucket()

# Create your views here.

def formatear_precio(precio):
    try:
        # Usar el formato de moneda para pesos colombianos (COP)
        return f"${precio:,.2f}"
    except (TypeError, ValueError):
        return "Precio no disponible"

def subir_imagen(image):
    blob = bucket.blob(f'productos/{image.name}')
    blob.upload_from_file(image, content_type=image.content_type)
    blob.make_public()
    return blob.public_url

def agregar_productos(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            # Obtener los datos del formulario
            nombre = form.cleaned_data['nombre']
            precio = form.cleaned_data['precio']
            stock = form.cleaned_data['stock']
            descripcion = form.cleaned_data['descripcion']
            imagen = request.FILES['imagen']
            
            imagen_url = subir_imagen(imagen)

            # Guardar el producto en Firestore
            db.collection('productos').add({
                'nombre': nombre,
                'precio': precio,
                'stock': stock,
                'descripcion': descripcion,
                'imagen_url': imagen_url,
            })

            return redirect('productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/agregar_productos.html', {'form': form})

def productos(request):
    productos_ref = db.collection('productos')
    docs = productos_ref.stream()

    productos = []
    for doc in docs:
        producto_data = doc.to_dict()
        producto_data['id'] = doc.id

        # Cambiar el nombre del producto si el stock es 0
        if producto_data.get('stock', 0) == 0:
            producto_data['nombre'] = 'Agotado'
        
        # Formatear el precio
        producto_data['precio_formateado'] = formatear_precio(producto_data.get('precio', 0))

        productos.append(producto_data)

    return render(request, 'productos.html', {'productos': productos})
