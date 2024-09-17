from django.shortcuts import render, redirect
from .forms import ContactForm
from firebase import db

# Create your views here.

def contacto(request):
    form = ContactForm()
    return render(request, 'contacto.html', {'form': form})

def crear_contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Limpiamos los datos y los guardamos en las keys
            datos = {
                'nombre': form.cleaned_data['nombre'],
                'apellido': form.cleaned_data['apellido'],
                'correo': form.cleaned_data['correo'],
                'descripcion': form.cleaned_data['descripcion'],
            }
            
            db.collection('solicitudes').add(datos)
            return redirect('contacto')
    else:
        form = ContactForm()
    return render(request, 'contacto.html', {'form': form})