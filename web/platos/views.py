from django.shortcuts import render

# Create your views here.

def platos(request):
    return render(request, "platos.html")