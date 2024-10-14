from django.shortcuts import render

# Create your views here.


def configuracion_administrador(request):
    return render(request, "configuracion_administrador.html")


def configuracion_sitio(request):
    return render(request, "configuracion_sitio.html")
