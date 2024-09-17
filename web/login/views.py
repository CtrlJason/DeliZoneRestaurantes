from django.shortcuts import render, redirect
from .forms import RegisterForm, AuthUserForm
from firebase import db
import bcrypt

# Create your views here.

def login(request):
    form = AuthUserForm
    return render(request, "login.html", {"form": form})

def autenticar_usuario(request):
    if request.method == "POST":
        form = AuthUserForm(request.POST)
        if form.is_valid():
            correo = form.cleaned_data["correo"]
            contraseña = form.cleaned_data["contraseña"]
            
            # Busca al usuario en Firebase
            user_ref = db.collection("clientes").where("correo", "==", correo).get()
            if len(user_ref) == 0:
                # En caso de que el usuario no este registrado
                return render(request, "login.html", {"form": form, "error": "Usuario no encontrado"})
            
            # Acceder a los datos del usuario
            for user in user_ref:
                user_data = user.to_dict()
                # Contraseña almacenada en Firestore, se almacenan para su posterior comparación
                stored_hashed_password = user_data["contraseña"]
                stored_salt = user_data["salt"]
            
            # Encriptar la contraseña ingresada por el usuario y comparar
            hashed_password = bcrypt.hashpw(contraseña.encode('utf-8'), stored_salt.encode('utf-8'))
            if hashed_password == stored_hashed_password:
                # Autenticacion exitosa
                return redirect("home")
            else:
                return render(request, "login.html", {"form": form, "error": "Contraseña Incorrecta"})
        else:
            form = AuthUserForm()
    else:
        form = AuthUserForm()
    return render(request, "login.html", {"form": form})

def register(request):
    form = RegisterForm
    return render(request, "register.html", {"form": form})

def registrar_usuario(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            apellido = form.cleaned_data["apellido"]
            correo = form.cleaned_data["correo"]
            contraseña = form.cleaned_data["contraseña"]
            
            # Generar el salt
            salt = bcrypt.gensalt()
            
            # Encriptar la contraseña utilizando el salt
            hashed_password = bcrypt.hashpw(contraseña.encode('utf-8'), salt)
            
            datos = {
                "nombre": nombre,
                "apellido": apellido,
                "correo": correo,
                "contraseña": hashed_password.decode('utf-8'),
                "salt": salt.decode('utf-8'), # Almacenar el salt
            }
            db.collection("clientes").add(datos)
            return redirect("login")
    else: form = RegisterForm
    return render(request, "register.html", {"form": form})