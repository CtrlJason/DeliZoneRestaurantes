from django.shortcuts import render, redirect
from .forms import ProductoForm
from firebase import db, bucket
from urllib.parse import urlparse

# Create your views here.

def formatear_precio(precio):
    try:
        # Usar el formato de moneda para pesos colombianos (COP)
        return f"${precio:,.2f}"
    # Mandamos un except en caso de que no se logre mostrar el precio
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
        if form.is_valid(): # se utiliza para validar los datos ingresados en un formulario
            # Obtenemos los datos del formulario
            nombre = form.cleaned_data['nombre']
            precio = form.cleaned_data['precio']
            stock = form.cleaned_data['stock']
            descripcion = form.cleaned_data['descripcion']
            imagen = request.FILES['imagen']
            
            # Guardamos el url de la imagen para llamarla en el template
            imagen_url = subir_imagen(imagen)

            # Guardar el producto en Firestore
            db.collection('productos').add({
                'nombre': nombre,
                'precio': precio,
                'stock': stock,
                'descripcion': descripcion,
                'imagen_url': imagen_url,
            })

            return redirect('productos') # Redirigimos al template 'productos'
    else:
        form = ProductoForm()
    return render(request, 'productos/agregar_productos.html', {'form': form})

def eliminar_producto(request, producto_id):
    # Guardamos la ubicacion de la coleccion en una variable
    producto_ref = db.collection('productos').document(producto_id)
    # Obtenemos los valores de la coleccion
    producto = producto_ref.get()
    
    if request.method == 'POST':
        # Elimina el producto en Firebase
        # Guardamos el url completo de la imagen
        imagen_url = producto.get('imagen_url')
        
        # Guardamos la ruta de la imagen con urlparse, este se usa para eliminar la parte del url antes del bucket
        ruta_archivo = urlparse(imagen_url).path # Extrae la ruta interna y esto devuelve '/[nombre_bucket]/ruta_Archivo.jpg'
        
        # Quitar el nombre del bucket del inicio de la ruta
        ruta_archivo = ruta_archivo.replace('/foodpartner-717d3.appspot.com/', '') # Reemplaza el nombre del bucket por un espacio vacio
        
        # Guardamos la ruta de la imagen
        imagen = bucket.blob(ruta_archivo)
        # Eliminamos la imagen y el producto
        imagen.delete()
        producto_ref.delete()
        
    return redirect('productos')

def editar_producto(request, producto_id):
    # Guardamos la ubicacion de la coleccion en una variable
    producto_ref = db.collection('productos').document(producto_id)
    # Obtenemos los valores de la coleccion
    producto = producto_ref.get()
    # Guardamos el url completo de la imagen
    
    # Guardamos la ubicacion de la coleccion en una variable
    producto_ref = db.collection('productos').document(producto_id)
    # Obtenemos los valores de la coleccion
    producto = producto_ref.get()
    # Guardamos el url completo de la imagen
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            # Actualizamos los datos del producto
            nombre = form.cleaned_data['nombre']
            precio = form.cleaned_data['precio']
            stock = form.cleaned_data['stock']
            descripcion = form.cleaned_data['descripcion']

            # Subimos nueva imagen solo si se ha cambiado
            if 'imagen' in request.FILES:
                imagen = request.FILES['imagen']
                imagen_url = subir_imagen(imagen)
            else:
                imagen_url = producto.get('imagen_url')

            # Actualizar el producto en Firestore
            producto_ref.update({
                'nombre': nombre,
                'precio': precio,
                'stock': stock,
                'descripcion': descripcion,
                'imagen_url': imagen_url,
            })
    else:
        # Pasa los datos actuales al formulario para que esté prellenado
        form = ProductoForm(initial={
            'nombre': producto.get('nombre'),
            'precio': producto.get('precio'),
            'stock': producto.get('stock'),
            'descripcion': producto.get('descripcion')
        })

    return render(request, 'productos', {'form': form, 'producto_id': producto_id})
        
        
        
    

def productos(request):
    productos_ref = db.collection('productos')
    docs = productos_ref.stream()

    productos = []
    for doc in docs:
        producto_data = doc.to_dict()
        producto_data['id'] = doc.id

        # Cambiar el nombre del producto si el stock es 0
        if producto_data.get('stock', 0) == 0:
            producto_data['precio'] = 'Agotado'
        
        # Formatear el precio
        producto_data['precio_formateado'] = formatear_precio(producto_data.get('precio', 0))

        productos.append(producto_data)

    return render(request, 'productos.html', {'productos': productos}) # Enviamos los productos al template 'productos'
