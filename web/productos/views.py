from django.shortcuts import render, redirect
from .forms import ProductoForm
from firebase import db, bucket

# Create your views here.

def productos(request):
    docs = db.collection("productos").get()
    productos = []
    for doc in docs:
        productos.append(doc.to_dict())
    return render(request, 'productos.html', {'productos': productos})

def subir_imagen(image):
    blob = bucket.blob(f'productos/{image.name}')
    blob.upload_from_file(image, content_type=image.content_type)
    blob.make_public()
    return blob.public_url

def agregar_productos(request):
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
            
            db.collection("productos").add(datos)
            
            return redirect("productos")
    else: 
        form = ProductoForm()
    return render(request, "agregar_productos.html", {'form': form})

def formatear_precio(precio):
        return

def eliminar_producto(request, producto_id):
    return redirect('productos')