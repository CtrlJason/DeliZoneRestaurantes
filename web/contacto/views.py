from django.shortcuts import render, redirect
from .forms import ContactForm
from firebase import db

# Create your views here.


def contacto(request):
    form = ContactForm()
    return render(request, "contacto.html", {"form": form})


def crear_contacto(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Limpiamos los datos y los guardamos en las keys
            datos = {
                "nombre": form.cleaned_data["nombre"],
                "celular": form.cleaned_data["celular"],
                "correo": form.cleaned_data["correo"],
                "asunto": form.cleaned_data["asunto"],
            }

            db.collection("restaurante1").document("web").collection("solicitudes").add(
                datos
            )
            return redirect("contacto")
    else:
        form = ContactForm()
    return render(request, "contacto.html", {"form": form})
