from django.shortcuts import render, redirect
from .forms import ProductoForm
from productos.productos import Productos
from firebase import db, bucket
from urllib.parse import urlparse

# Create your views here.

def productos(request):
    # Formulario productos
    form = ProductoForm()
    # Productos
    lista_productos = Productos.tienda_productos()
    lista_categorias = Productos.categorias()
    if 'administradores_id' not in request.session:
        return redirect('acceder_administrador')
    else:
        context = {
            'form': form,
            'lista_productos': lista_productos,
            'lista_categorias': lista_categorias
        }
        return render(request, 'productos.html', context)

def subir_imagen(image):
    blob = bucket.blob(f'restaurante1/productos/{image.name}')
    blob.upload_from_file(image, content_type=image.content_type)
    blob.make_public()
    return blob.public_url

def agregar_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            precio = form.cleaned_data['precio']
            stock = form.cleaned_data['stock']
            imagen = request.FILES['imagen']
            descripcion = form.cleaned_data['descripcion']
            
            imagen_url = subir_imagen(imagen)
            
            datos = {
                'nombre' : nombre,
                'precio' : precio,
                'stock' : stock,
                'imagen' : imagen_url,
                'descripcion' : descripcion
            }
            
            db.collection('restaurante1').document('web').collection('productos').add(datos)
            return redirect("productos")
    else: 
        form = ProductoForm()
    return redirect('productos')

def eliminar_producto(request, producto_id):
    # Guardamos la ubicacion de la coleccion en una variable
    producto_ref = db.collection('restaurante1').document('web').collection('productos').document(producto_id)
    # Obtenemos los valores de la coleccion
    producto = producto_ref.get()
    if request.method == 'POST':
        # Elimina el producto en Firebase
        # Guardamos el url completo de la imagen
        imagen_url = producto.get('imagen')
        # Guardamos la ruta de la imagen con urlparse, este se usa para eliminar la parte del url antes del bucket
        ruta_archivo = urlparse(imagen_url).path # Extrae la ruta interna y esto devuelve '/[nombre_bucket]/ruta_Archivo.jpg'
        # Quitar el nombre del bucket del inicio de la ruta
        ruta_archivo = ruta_archivo.replace('/delizone-1a227.appspot.com/', '') # Reemplaza el nombre del bucket por un espacio vacio
        # Guardamos la ruta de la imagen
        imagen = bucket.blob(ruta_archivo)
        # Eliminamos la imagen y el producto
        imagen.delete()
        producto_ref.delete()
    return redirect('productos')

def crear_categoria(request):
    
    return