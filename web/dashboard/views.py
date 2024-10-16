from django.shortcuts import render, redirect
from firebase import db
from gestion_acceso.forms import RegistroAdministradoresForm, RegistroEmpleadoForm


# Create your views here.


def dashboard(request):
    if "administradores_id" not in request.session:
        return redirect("acceder_administrador")
    else:
        return render(request, "dashboard.html")


def home(request):
    if "administradores_id" not in request.session:
        return redirect("acceder_administrador")
    else:
        return render(request, "index.html")


# --=================== VISTA EMPLEADOS Y ADMINISTRADORES ===================-- #


def ver_usuarios(request):
    form_empleados = RegistroEmpleadoForm()
    form_administradores = RegistroAdministradoresForm()
    docs_empleados = (
        db.collection("restaurante1")
        .document("usuarios")
        .collection("empleados")
        .stream()
    )
    docs_administradores = (
        db.collection("restaurante1")
        .document("usuarios")
        .collection("administradores")
        .order_by("apellidos")
        .stream()
    )

    lista_empleados = []
    lista_administradores = []
    contador = 0

    # Guardamos a los empleados para mostrarlos en el template
    for doc in docs_empleados:
        datos_empleado = doc.to_dict()
        datos_empleado["id"] = doc.id
        lista_empleados.append(datos_empleado)
        contador += 1

    # Guardamos a los empleados para mostrarlos en el template
    for doc in docs_administradores:
        datos_administrador = doc.to_dict()
        datos_administrador["id"] = doc.id
        lista_administradores.append(datos_administrador)
        contador += 1

    if "administradores_id" not in request.session:
        return redirect("acceder_administrador")
    else:
        context = {
            "lista_empleados": lista_empleados,
            "lista_administradores": lista_administradores,
            "form_empleados": form_empleados,
            "form_administradores": form_administradores,
        }
        return render(request, "usuarios.html", context)
