from django.shortcuts import render
from firebase import db

# Create your views here.

def menu(request):
    docs = db.collection("productos").get()
    lista_productos = []
    for doc in docs:
        lista_productos.append(doc.to_dict)
    return render(request, "menu.html", {"lista_productos": lista_productos})