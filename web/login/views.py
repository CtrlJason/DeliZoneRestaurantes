from django.shortcuts import render, redirect
from firebase import db

# Create your views here.

def login(request):
    return render(request, "login.html")