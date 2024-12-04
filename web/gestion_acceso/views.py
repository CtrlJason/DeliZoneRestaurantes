from django.shortcuts import render, redirect
from .forms import (
    RegistroClienteForm,
    AccederUsuarioForm,
    RegistroUsuarioForm
)
from firebase import db, bucket
from urllib.parse import urlparse
import bcrypt

# --=================== ACCESO USUARIOS ===================-- #

def acceder_usuario(request, coleccion, datos_redireccion):
    if request.method == "POST":
        form = AccederUsuarioForm(request.POST)
        if form.is_valid():
            # Informacion del formulario
            correo = form.cleaned_data["correo"].lower().strip()
            password = form.cleaned_data["password"]
            #  Buscar en la base de datos
            usuario_ref = (
                db.collection("restaurante1").document("usuarios").collection(coleccion)
            )
            query = usuario_ref.where("correo", "==", correo).get()
            if query:
                usuario = query[0].to_dict()
                password_encriptada = usuario["password"]
                if bcrypt.checkpw(password.encode(), password_encriptada.encode()):
                    usuario_id = query[0].id
                    request.session[f"{coleccion}_id"] = usuario_id
                    if "carrito" in request.session:
                        del request.session["carrito"]
                    return redirect(datos_redireccion)
                else:
                    form.add_error(None, "La contraseña es incorrecta")
            else:
                form.add_error(None, "No se encontró un usuario con este correo")
    else:
        form = AccederUsuarioForm()
    return render(request, f"{coleccion}/acceder_{coleccion}.html", {"form": form})


def acceder_cliente(request):
    return acceder_usuario(request, "clientes", "home")


def acceder_administrador(request):
    return acceder_usuario(request, "administradores", "admin")


# --=================== CERRAR SESIONES USUARIOS ===================-- #

def cerrar_session_cliente(request):
    del request.session["clientes_id"]
    return redirect("acceder_cliente")


def cerrar_session_administrador(request):
    del request.session["administradores_id"]
    return redirect("acceder_administrador")


# --=================== SUBIR IMAGENES ===================-- #


def subir_imagen(image):
    blob = bucket.blob(f"restaurante1/usuarios/{image.name}")
    blob.upload_from_file(image, content_type=image.content_type)
    blob.make_public()
    return blob.public_url


# --=================== REGISTRO CLIENTES ===================-- #

def registro_cliente(request):
    if request.method == "POST":
        form = RegistroClienteForm(request.POST)
        # Verificamos si el formulario que relleno el usuario es valido para poder realizar el registro del mismo
        if form.is_valid():
            nombres = form.cleaned_data["nombres"]
            apellidos = form.cleaned_data["apellidos"]
            correo = form.cleaned_data["correo"].lower().strip()
            celular = form.cleaned_data["celular"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]

            if password1 != password2:
                form.add_error("password2", "las contraseñas no coinciden")
            else:
                # Encriptamos la contraseña en caso de que el usuario haya puesto las contraseñas correctamente
                password_encriptada = bcrypt.hashpw(password1.encode(), bcrypt.gensalt()).decode("utf-8")
                # Verificamos que el correo no haya sido registrado por otro usuario
                query = (
                    db.collection("restaurante1")
                    .document("usuarios")
                    .collection("clientes")
                    .where("correo", "==", correo)
                    .get()
                )
                if len(query) > 0:
                    form.add_error(None, "El administrador ya se encuentra registrado.")
                else:
                    try:
                        db.collection("restaurante1").document("usuarios").collection(
                            "clientes"
                        ).add(
                            {
                                "nombres": nombres,
                                "apellidos": apellidos,
                                "correo": correo,
                                "celular": celular,
                                "password": password_encriptada,
                                "imagen": "https://firebasestorage.googleapis.com/v0/b/delizone-1a227.appspot.com/o/DeliZone%2FCliente%2Fuser-circle-black.svg?alt=media&token=667e6bbd-7acb-4655-b5cb-697347ef3883",
                                "direccion": {}
                            }
                        )
                        return redirect("acceder_cliente")
                    except Exception as e:
                        form.add_error(None, f"Error al registrar el usuario: {e}")
    else:
        form = RegistroClienteForm()
    return render(request, "clientes/registro_cliente.html", {"form": form})


# --=================== REGISTRO USUARIOS ADMINISTRACIÓN ===================-- #

def registro_usuario(request, db_usuario, nombre_usuario):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            nombres = form.cleaned_data["nombres"]
            apellidos = form.cleaned_data["apellidos"]
            correo = form.cleaned_data["correo"].lower().strip()
            password = form.cleaned_data["password"]
            cargo = form.cleaned_data["cargo"]
            # Encriptamos la contraseña
            password_encriptada = bcrypt.hashpw(
                password.encode(), bcrypt.gensalt()
            ).decode("utf-8")
            
            usuarios_ref = (
                db.collection("restaurante1")
                .document("usuarios")
                .collection(db_usuario)
            )
            
            query = usuarios_ref.where("correo", "==", correo).get()
            if len(query) > 0:
                form.add_error(None, f"El {nombre_usuario} ya se encuentra registrado.")
            try:
                imagen_url = "https://firebasestorage.googleapis.com/v0/b/delizone-1a227.appspot.com/o/DeliZone%2FCliente%2Fuser-circle-black.svg?alt=media&token=667e6bbd-7acb-4655-b5cb-697347ef3883"
                if "imagen" in request.FILES:
                    imagen = request.FILES["imagen"]
                    imagen_url = subir_imagen(imagen)
                usuarios_ref.add(
                    {
                        "nombres": nombres,
                        "apellidos": apellidos,
                        "correo": correo,
                        "password": password_encriptada,
                        "cargo": cargo,
                        "rol": nombre_usuario,
                        "estado": True,
                        "imagen": imagen_url,
                    }
                )
            except Exception as e:
                form.add_error(None, "Error al registrar al empleado")
    else:
        form = RegistroUsuarioForm()
    return redirect("ver_usuarios")

# --=================== ELIMINAR CLIENTES-EMPLEADOS-ADMINISTRADORES ===================-- #

def eliminar_usuarios(request, id_usuario, coleccion):
    usuario_ref = (
        db.collection("restaurante1")
        .document("usuarios")
        .collection(coleccion)
        .document(id_usuario)
    )
    usuario = usuario_ref.get()
    if request.method == "POST":
        # Guardamos el url completo de la imagen
        imagen_url = usuario.get("imagen")
        # Guardamos la ruta de la imagen con urlparse, este se usa para eliminar la parte del url antes del bucket
        ruta_archivo = urlparse(imagen_url).path
        # Reemplaza el nombre del bucket por un espacio vacio
        ruta_archivo = ruta_archivo.replace("/delizone-1a227.appspot.com/", "")
        imagen = bucket.blob(ruta_archivo)
        try:
            imagen.delete()
        except Exception as e:
            print(f"Hubo un error al eliminar la imagen, puede que esta no exista")
        usuario_ref.delete()
    return redirect("ver_usuarios")


def eliminar_cliente(request, id_cliente):
    return eliminar_usuarios(request, id_cliente, "clientes")

def eliminar_empleado(request, id_empleado):
    return eliminar_usuarios(request, id_empleado, "empleados")

def eliminar_administrador(request, id_administrador):
    if id_administrador == request.session["administradores_id"]:
        print("No se puede eliminar al administrador ya que cuenta con la sesion activa")
        return redirect('ver_usuarios')
    else:
        return eliminar_usuarios(request, id_administrador, "administradores")
