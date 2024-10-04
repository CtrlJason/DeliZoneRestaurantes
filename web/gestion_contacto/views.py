from django.shortcuts import render, redirect
from firebase import db

# Create your views here.

def gestion_contacto(request):
    docs = db.collection('restaurante1').document('web').collection('solicitudes').stream()
    formularios = []
    for doc in docs:
        formularios_data = doc.to_dict()
        formularios_data['id'] = doc.id
        formularios.append(formularios_data)
    return render(request, "gestion_contacto.html", {"formularios": formularios})


def eliminar_formulario(request, formulario_id):
    if request.method == "POST":
        db.collection('restaurante1').document('web').collection('solicitudes').document(formulario_id).delete()
    return redirect('gestion_contacto')