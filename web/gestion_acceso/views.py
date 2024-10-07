from django.shortcuts import render, redirect
from .forms import RegistroClienteForm, AccederUsuarioForm, RegistroEmpleadoForm, RegistroAdministradoresForm
from firebase import db, bucket
from urllib.parse import urlparse
import bcrypt

# --=================== ACCESO USUARIOS ===================-- #

def acceder_usuario(request, coleccion, redirect_data):
    if request.method == 'POST':
        form = AccederUsuarioForm(request.POST)
        if form.is_valid():
            # Informacion del formulario
            correo = form.cleaned_data['correo'].lower().strip()
            contraseña = form.cleaned_data['contraseña']
            #  Buscar en la base de datos
            usuario_ref = db.collection('restaurante1').document('usuarios').collection(coleccion)
            query = usuario_ref.where("correo", "==", correo).get()
            if query:
                usuario = query[0].to_dict()
                contraseña_encriptada = usuario['contraseña']
                if bcrypt.checkpw(contraseña.encode(), contraseña_encriptada.encode()):
                    usuario_id = query[0].id
                    request.session[f'{coleccion}_id'] = usuario_id
                    if 'carrito' in request.session:
                        del request.session['carrito']
                    return redirect(redirect_data)
                else:
                    form.add_error(None, "La contraseña es incorrecta")
            else:
                form.add_error(None, "No se encontró un usuario con este correo")
    else:
        form = AccederUsuarioForm()
    return render(request, f"{coleccion}/acceder_{coleccion}.html", {'form': form})

def acceder_cliente(request):
    return acceder_usuario(request, 'clientes','home')

def acceder_administrador(request):
    return acceder_usuario(request, 'administradores', 'admin')

# --=================== CERRAR SESIONES USUARIOS ===================-- #

def cerrar_session_cliente(request):
    del request.session['clientes_id']
    return redirect('acceder_cliente')

def cerrar_session_administrador(request):
    del request.session['administradores_id']
    return redirect('acceder_administrador')

# --=================== SUBIR IMAGENES ===================-- #

def subir_imagen(image):
    blob = bucket.blob(f'restaurante1/usuarios/{image.name}')
    blob.upload_from_file(image, content_type=image.content_type)
    blob.make_public()
    return blob.public_url

# --=================== REGISTRO CLIENTES ===================-- #

def registro_cliente(request):
    if request.method == "POST":
        form = RegistroClienteForm(request.POST)
        # Verificamos si el formulario que relleno el usuario es valido para poder realizar el registro del mismo
        if form.is_valid():
            nombres = form.cleaned_data['nombres']
            apellidos = form.cleaned_data['apellidos']
            correo = form.cleaned_data['correo'].lower().strip()
            celular = form.cleaned_data['celular']
            contraseña1 = form.cleaned_data['contraseña1']
            contraseña2 = form.cleaned_data['contraseña2']
            
            if contraseña1 != contraseña2:
                form.add_error('contraseña2', 'las contraseñas no coinciden')
            else:
                # Encriptamos la contraseña en caso de que el usuario haya puesto las contraseñas correctamente
                contraseña_encriptada = bcrypt.hashpw(contraseña1.encode(), bcrypt.gensalt()).decode('utf-8')
                # Verificamos que el correo no haya sido registrado por otro usuario
                query = db.collection('restaurante1').document('usuarios').collection('clientes').where("correo", "==", correo).get()
                if len(query) > 0:
                    form.add_error(None, "El administrador ya se encuentra registrado.")
                else:
                    try:
                        db.collection('restaurante1').document('usuarios').collection('clientes').add({
                            'nombres': nombres,
                            'apellidos': apellidos,
                            'correo': correo,
                            'celular': celular,
                            'contraseña': contraseña_encriptada,
                            'imagen': 'https://firebasestorage.googleapis.com/v0/b/delizone-1a227.appspot.com/o/DeliZone%2FCliente%2Fuser-circle-black.svg?alt=media&token=667e6bbd-7acb-4655-b5cb-697347ef3883'
                        })
                        return redirect('acceder_cliente')
                    except Exception as e:
                        form.add_error(None, f"Error al registrar el usuario: {e}")
    else:
        form = RegistroClienteForm()
    return render(request, "clientes/registro_cliente.html", {'form': form})

# --=================== REGISTRO EMPLEADOS ===================-- #

def registro_empleado(request):
    if request.method == "POST":
        form = RegistroEmpleadoForm(request.POST,  request.FILES)

        if form.is_valid():
            nombres = form.cleaned_data['nombres']
            apellidos = form.cleaned_data['apellidos']
            correo = form.cleaned_data['correo'].lower().strip()
            contraseña = form.cleaned_data['contraseña']
            cargo = form.cleaned_data['cargo']
            
            # Encriptamos la contraseña
            contraseña_encriptada = bcrypt.hashpw(contraseña.encode(), bcrypt.gensalt()).decode('utf-8')
            
            usuarios_ref = db.collection('restaurante1').document('usuarios').collection('empleados')
            query = usuarios_ref.where("correo", "==", correo).get()
            if len(query) > 0:
                form.add_error(None, "El administrador ya se encuentra registrado.")
            try:
                imagen_url = "https://firebasestorage.googleapis.com/v0/b/delizone-1a227.appspot.com/o/DeliZone%2FCliente%2Fuser-circle-black.svg?alt=media&token=667e6bbd-7acb-4655-b5cb-697347ef3883"
                if 'imagen' in request.FILES:
                    imagen = request.FILES['imagen']
                    imagen_url = subir_imagen(imagen)
                usuarios_ref.add({
                    'nombres':nombres,
                    'apellidos':apellidos,
                    'correo':correo,
                    'contraseña':contraseña_encriptada,
                    'cargo':cargo,
                    'rol': 'empleado',
                    'estado': True,
                    'imagen': imagen_url
                    })
            except Exception as e:
                form.add_error(None, 'Error al registrar al empleado')
    else:
        form = RegistroEmpleadoForm()
    return redirect('ver_usuarios')

# --=================== REGISTRO ADMINISTRADORES ===================-- #

def registro_administrador(request):
    if request.method == "POST":
        form = RegistroAdministradoresForm(request.POST, request.FILES)
        if form.is_valid():
            nombres = form.cleaned_data['nombres']
            apellidos = form.cleaned_data['apellidos']
            correo = form.cleaned_data['correo'].lower().strip()
            contraseña = form.cleaned_data['contraseña']
            
            # Encriptamos la contraseña
            contraseña_encriptada = bcrypt.hashpw(contraseña.encode(), bcrypt.gensalt()).decode('utf-8')
            
            usuarios_ref = db.collection('restaurante1').document('usuarios').collection('administradores')
            query = usuarios_ref.where("correo", "==", correo).get()
            if len(query) > 0:
                form.add_error(None, "El administrador ya se encuentra registrado.")
            else:
                try:
                    imagen_url = "https://firebasestorage.googleapis.com/v0/b/delizone-1a227.appspot.com/o/DeliZone%2FCliente%2Fuser-circle-black.svg?alt=media&token=667e6bbd-7acb-4655-b5cb-697347ef3883"
                    if 'imagen' in request.FILES:
                        imagen = request.FILES['imagen']
                        imagen_url = subir_imagen(imagen)
                    usuarios_ref.add({
                    'nombres':nombres,
                    'apellidos':apellidos,
                    'correo':correo,
                    'contraseña':contraseña_encriptada,
                    'rol': 'admin',
                    'estado': True,
                    'imagen': imagen_url
                    })
                except Exception as e:
                    form.add_error(None, 'Error al registrar al empleado')
    else:
        form = RegistroEmpleadoForm()
    return redirect('ver_usuarios')

# --=================== VISTA EMPLEADOS Y ADMINISTRADORES ===================-- #

def ver_usuarios(request):
    form_empleados = RegistroEmpleadoForm()
    form_administradores = RegistroAdministradoresForm()
    docs_empleados = db.collection('restaurante1').document('usuarios').collection('empleados').stream()
    docs_administradores = db.collection('restaurante1').document('usuarios').collection('administradores').stream()
    
    lista_empleados = []
    lista_administradores = []
    contador = 0
    
    # Guardamos a los empleados para mostrarlos en el template
    for doc in docs_empleados:
        datos_empleado = doc.to_dict()
        datos_empleado['id'] = doc.id
        lista_empleados.append(datos_empleado)
        contador+=1
        
    # Guardamos a los empleados para mostrarlos en el template
    for doc in docs_administradores:
        datos_administrador = doc.to_dict()
        datos_administrador['id'] = doc.id
        lista_administradores.append(datos_administrador)
        contador+=1
        
    if 'administradores_id' not in request.session:
        return redirect('acceder_administrador')
    else:
        context = {
            'lista_empleados':lista_empleados,
            'lista_administradores':lista_administradores,
            'form_empleados': form_empleados,
            'form_administradores': form_administradores,
        }
        return render(request, 'usuarios/usuarios.html', context)
        
# --=================== ELIMINAR CLIENTES-EMPLEADOS-ADMINISTRADORES ===================-- #

def eliminar_usuarios(request, id_usuario, coleccion):
    usuario_ref = db.collection('restaurante1').document('usuarios').collection(coleccion).document(id_usuario)
    usuario = usuario_ref.get()
    if request.method == 'POST':
        # Guardamos el url completo de la imagen
        imagen_url = usuario.get('imagen')
        # Guardamos la ruta de la imagen con urlparse, este se usa para eliminar la parte del url antes del bucket
        ruta_archivo = urlparse(imagen_url).path
        # Reemplaza el nombre del bucket por un espacio vacio
        ruta_archivo = ruta_archivo.replace('/delizone-1a227.appspot.com/', '')
        imagen = bucket.blob(ruta_archivo)
        try: 
            imagen.delete()
        except Exception as e:
            print(f"Hubo un error al eliminar la imagen, puede que esta no exista")
        usuario_ref.delete()
    return redirect('ver_usuarios')

def eliminar_cliente(request, id_cliente):
    return eliminar_usuarios(request, id_cliente, 'clientes')

def eliminar_empleado(request, id_empleado):
    return eliminar_usuarios(request, id_empleado, 'empleados')

def eliminar_administrador(request, id_administrador):
    return eliminar_usuarios(request, id_administrador, 'administradores')