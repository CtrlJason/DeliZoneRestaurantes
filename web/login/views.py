from django.shortcuts import render, redirect
from .forms import RegisterForm, AuthUserForm
from firebase import db

# Create your views here.

def login(request):
    return render(request, "login.html")

def autenticar_usuario(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def registrar_usuario(request):
    return render(request, "register.html")