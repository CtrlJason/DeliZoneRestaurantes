from django.shortcuts import render, redirect
from firebase import db


# Create your views here.

def dashboard(request):
    if 'administradores_id' not in request.session:
        return redirect('acceder_administrador')
    else:
        return render(request, "dashboard.html")

def home(request):
    if 'administradores_id' not in request.session:
        return redirect('acceder_administrador')
    else:
        return render(request, "index.html")