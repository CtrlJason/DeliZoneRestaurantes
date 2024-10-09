from django.shortcuts import render

# Create your views here.

def ubicacion(request):
    return render(request, "ubicacion.html")