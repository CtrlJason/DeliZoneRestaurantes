from django.shortcuts import render, redirect
from .forms import ContactForm
from firebase import db

# Create your views here.

def contacto(request):
    # Contador del carrito de compras
    docs_car = db.collection('carrito').stream()
    cantidad_productos = 0

    for i in docs_car:
        cantidad_productos += 1
        
    form = ContactForm()
    return render(request, 'contacto.html', {'form': form, 'cantidad_productos': cantidad_productos})

def crear_contacto(request):    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Limpiamos los datos y los guardamos en las keys
            datos = {
                'nombre': form.cleaned_data['nombre'],
                'celular': form.cleaned_data['celular'],
                'correo': form.cleaned_data['correo'],
                'asunto': form.cleaned_data['asunto'],
            }
            
            db.collection('solicitudes').add(datos)
            return redirect('contacto')
    else:
        form = ContactForm()
    return render(request, 'contacto.html', {'form': form})