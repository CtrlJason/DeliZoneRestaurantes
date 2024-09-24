from django.shortcuts import render
from productos.views import formatear_precio
from firebase import db


# Create your views here.

def dashboard(request):
    return render(request, "dashboard.html")