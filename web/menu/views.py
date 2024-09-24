from django.shortcuts import render
from firebase import db
from productos.views import formatear_precio

# Create your views here.

def menu(request):
    return render(request, "menu.html")