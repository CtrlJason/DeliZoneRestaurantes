from django.shortcuts import render
from firebase import db


# Create your views here.

def dashboard(request):
    return render(request, "dashboard.html")