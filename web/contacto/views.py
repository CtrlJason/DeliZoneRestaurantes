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
                'celular': form.cleaned_data['celular'],
                'correo': form.cleaned_data['correo'],
                'asunto': form.cleaned_data['asunto'],
            }
            
            db.collection('solicitudes').add(datos)
            return redirect('contacto')
    else:
        form = ContactForm()
    return render(request, 'contacto.html', {'form': form})


def ver_formularios(request):
    forms_ref = db.collection("solicitudes")
    docs = forms_ref.stream()
    formularios = []
    for doc in docs:
        formularios_data = doc.to_dict()
        formularios_data['id'] = doc.id
        formularios.append(formularios_data)
    return render(request, "ver_formularios.html", {"formularios": formularios})


def eliminar_formulario(request, formulario_id):
    if request.method == "POST":
        db.collection("solicitudes").document(formulario_id).delete()
    return redirect('ver_formularios')