from django.shortcuts import render

# Create your views here.

def perfil_user(request):
    return render(request, "perfil_user.html")