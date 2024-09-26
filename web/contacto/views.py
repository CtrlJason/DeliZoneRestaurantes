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
        form = ContactForm(request.POST)
        if form.is_valid():
            # Limpiamos los datos y los guardamos en las keys
            # datos = {
            #     'nombre': form.cleaned_data['nombre'],
            #     'celular': form.cleaned_data['celular'],
            #     'correo': form.cleaned_data['correo'],
            #     'asunto': form.cleaned_data['asunto'],
            # }
            
            name = request.POST['name']
            email = request.POST['email']
            correo = request.POST['correo']
            mesagge = request.POST['mesagge']
            from_email = settings.EMAIL_HOST_USER
            destinatario = ["guini753@gmail.com"]
            
            # db.collection('solicitudes').add(datos)
            
            send_mail(name, email, correo, mesagge, from_email, destinatario)
            
            return redirect('contacto')
    else:
        form = ContactForm()
    return render(request, 'contacto.html', {'form': form})

def ver_formularios(request):
    forms = db.collection("solicitudes").get()
    formularios = []
    for form in forms:
        formularios.append(form.to_dict())
    print(formularios)
    return render(request, "ver_formularios.html", {"formularios" : formularios})