from django.shortcuts import render, redirect
from .forms import ContactForm
from firebase import db
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def contacto(request):
    form = ContactForm()
    return render(request, 'contacto.html', {'form': form})

def crear_contacto(request):
    if request.method == 'POST':
        # Limpiamos los datos y los guardamos en las keys
        # datos = {
        #     'nombre': form.cleaned_data['nombre'],
        #     'celular': form.cleaned_data['celular'],
        #     'correo': form.cleaned_data['correo'],
        #     'asunto': form.cleaned_data['asunto'],
        # }
        
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        mesagge = request.POST['mesagge']
        from_email = settings.EMAIL_HOST_USER
        destinatario = ["yeisondamosquera@gmail.com"]
        # db.collection('solicitudes').add(datos)
        
        send_mail(subject, mesagge, from_email, destinatario)
        return redirect('contacto')
    return render(request, 'contacto.html')

def ver_formularios(request):
    forms = db.collection("solicitudes").get()
    formularios = []
    for form in forms:
        formularios.append(form.to_dict())
    print(formularios)
    return render(request, "ver_formularios.html", {"formularios" : formularios})