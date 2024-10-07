from django.shortcuts import render, redirect
from .forms import ContactForm
from firebase import db
from gestion_acceso.acceso import estado_login

# Create your views here.

def contacto(request):
    form = ContactForm()
    login = estado_login(request)
    return render(request, 'contacto.html', {
        'form': form,
        'login': login
        })

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
            
            db.collection('restaurante1').document('web').collection('solicitudes').add(datos)
            return redirect('contacto')
    else:
        form = ContactForm()
    return render(request, 'contacto.html', {'form': form})