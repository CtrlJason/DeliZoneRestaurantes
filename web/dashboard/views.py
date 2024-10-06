from django.shortcuts import render
from firebase import db
from .usuarios import UsuarioAdministrador


# Create your views here.

def dashboard(request):
    return render(request, "dashboard.html")

def home(request):
    imagen_administrador = UsuarioAdministrador.imagen_admin()
    return render(request, "index.html", {"imagen_administrador": imagen_administrador})