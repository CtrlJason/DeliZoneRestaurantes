from django.shortcuts import render

# Create your views here.

def home(request): # llamar al modulo igual que al index
    return render(request, "home.html")