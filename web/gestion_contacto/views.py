from django.shortcuts import render, redirect
from firebase import db

# Create your views here.

def gestion_contacto(request):
    forms_ref = db.collection("solicitudes")
    docs = forms_ref.stream()
    formularios = []
    for doc in docs:
        formularios_data = doc.to_dict()
        formularios_data['id'] = doc.id
        formularios.append(formularios_data)
    return render(request, "gestion_contacto.html", {"formularios": formularios})


def eliminar_formulario(request, formulario_id):
    if request.method == "POST":
        db.collection("solicitudes").document(formulario_id).delete()
    return redirect('gestion_contacto')