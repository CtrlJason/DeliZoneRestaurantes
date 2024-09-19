from django.shortcuts import render

# Create your views here.

def perfil_user(requirement):
    return render(requirement, "perfil_user.html")