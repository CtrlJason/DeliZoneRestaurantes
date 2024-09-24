from django.shortcuts import render
from firebase import db

# Create your views here.

def home(request):
    return render(request, 'home.html')