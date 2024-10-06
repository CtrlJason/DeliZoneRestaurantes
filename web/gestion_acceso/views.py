from django.shortcuts import render, redirect
from dashboard.usuarios import UsuarioAdministrador
from .forms import RegistroClienteForm, AccederUsuarioForm, RegistroEmpleadoForm, RegistroAdministradoresForm
from firebase import db
import bcrypt

# --=================== CLIENTES ===================-- #

def registro_cliente(request):
    if request.method == "POST":
        form = RegistroClienteForm(request.POST)
        # Verificamos si el formulario que relleno el usuario es valido para poder realizar el registro del mismo
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            correo = form.cleaned_data['correo']
            celular = form.cleaned_data['celular']
            contraseña1 = form.cleaned_data['contraseña1']
            contraseña2 = form.cleaned_data['contraseña2']
            
            if contraseña1 != contraseña2:
                form.add_error('contraseña2', 'las contraseñas no coinciden')
            else:
                # Encriptamos la contraseña en caso de que el usuario haya puesto las contraseñas correctamente
                contraseña_encriptada = bcrypt.hashpw(contraseña1.encode(), bcrypt.gensalt()).decode('utf-8')
                # Verificamos que el correo no haya sido registrado por otro usuario
                query = db.collection('restaurante1').document('usuarios').collection('clientes').where("email", "==", correo).get()
                if query:
                    form.add_error(None, "El correo ya se encuentra registrado.")
                else:
                    try:
                        db.collection('restaurante1').document('usuarios').collection('clientes').add({
                            'nombres': nombre,
                            'apellidos': apellido,
                            'correo': correo,
                            'celular': celular,
                            'contraseña': contraseña_encriptada,
                            'imagen': 'https://firebasestorage.googleapis.com/v0/b/foodpartner-717d3.appspot.com/o/iconos%2Fnavbar%2Fuser.svg?alt=media&token=46662fea-4c7e-45e8-8827-0223d51507c4'
                        })
                        return redirect('acceder_cliente')
                    except Exception as e:
                        form.add_error(None, f"Error al registrar el usuario: {e}")
    else:
        form = RegistroClienteForm()
    return render(request, "clientes/registro_cliente.html", {'form': form})

def acceder_cliente(request):
    if request.method == "POST":
        form = AccederUsuarioForm(request.POST)
        if form.is_valid():
            # Traemos el correo y la contraseña proporcionada por el usuario
            correo = form.cleaned_data['correo']
            contraseña = form.cleaned_data['contraseña']
            
            # Traemos a todos los clientes de la base de datos
            usuario_ref = db.collection('restaurante1').document('usuarios').collection('clientes')
            # Verificamos que el correo que proporciono el usuario exista
            query = usuario_ref.where("correo", "==", correo).get()
            
            # Si el correo existe se cumple esta condificon
            if query:
                # Traemos los datos del usuario con base al correo
                cliente = query[0].to_dict()
                # Guardamos la contraseña del usuario en una variable para compararla
                contraseña_encriptada = cliente['contraseña']
                # Verificamos ambas contraseñas, tanto la encriptada como la proporicionada por el usuario, esta ultima se encripta para que coincida con la guardada en la base de datos
                if bcrypt.checkpw(contraseña.encode(), contraseña_encriptada.encode()): #contraseña_encriptada.encode(): esto convierte la contraseña encriptada (que fue almacenada en la base de datos) en bytes para que bcrypt pueda realizar la comparación.
                    return redirect('home')
                else:
                    form.add_error(None, "La contraseña es incorrecta")
            # Si no existe se cumple el else
            else:
                form.add_error(None, "No se encontró un usuario con este correo")
    else:
        form = AccederUsuarioForm()
    return render(request, "clientes/acceder_cliente.html", {'form': form})

# --=================== REGISTRO EMPLEADOS ===================-- #

def registro_empleado(request):
    if request.method == "POST":
        form = RegistroEmpleadoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            correo = form.cleaned_data['correo']
            contraseña = form.cleaned_data['contraseña']
            cargo = form.cleaned_data['cargo']
            
            # Encriptamos la contraseña
            contraseña_encriptada = bcrypt.hashpw(contraseña.encode(), bcrypt.gensalt()).decode('utf-8')
            
            query = db.collection('restaurante1').document('usuarios').collection('empleados').where("email", "==", correo).get()
            if query:
                form.add_error(None, "El empleado ya se encuentra registrado.")
            else:
                try:
                    db.collection('restaurante1').document('usuarios').collection('empleados').add({
                        'nombre':nombre,
                        'apellido':apellido,
                        'correo':correo,
                        'contraseña':contraseña_encriptada,
                        'cargo':cargo,
                        'rol': 'empleado',
                        'estado': True,
                        'imagen': 'https://firebasestorage.googleapis.com/v0/b/foodpartner-717d3.appspot.com/o/iconos%2Ficons-dashboard%2Fmenu-arriba%2Fuser-circle-black.svg?alt=media&token=0959a85e-d15a-43d9-b458-09009b2b96c7'
                    })
                except Exception as e:
                    form.add_error(None, 'Error al registrar al empleado')
    else:
        form = RegistroEmpleadoForm()
    return redirect('ver_usuarios')

# --=================== REGISTRO ADMINISTRADORES ===================-- #

def registro_administrador(request):
    if request.method == "POST":
        form = RegistroAdministradoresForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            correo = form.cleaned_data['correo']
            contraseña = form.cleaned_data['contraseña']
            
            # Encriptamos la contraseña
            contraseña_encriptada = bcrypt.hashpw(contraseña.encode(), bcrypt.gensalt()).decode('utf-8')
            
            query = db.collection('restaurante1').document('usuarios').collection('administradores').where("email", "==", correo).get()
            if query:
                form.add_error(None, "El administrador ya se encuentra registrado.")
            else:
                try:
                    db.collection('restaurante1').document('usuarios').collection('administradores').add({
                        'nombre':nombre,
                        'apellido':apellido,
                        'correo':correo,
                        'contraseña':contraseña_encriptada,
                        'rol': 'admin',
                        'estado': True,
                        'imagen': "https://firebasestorage.googleapis.com/v0/b/foodpartner-717d3.appspot.com/o/iconos%2Ficons-dashboard%2Fmenu-arriba%2Fuser-circle-black.svg?alt=media&token=0959a85e-d15a-43d9-b458-09009b2b96c7"
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
    
    for doc in docs_empleados:
        lista_empleados.append(doc.to_dict())
    for doc in docs_administradores:
        lista_administradores.append(doc.to_dict())
    # Imagen del administrador
    imagen_administrador = UsuarioAdministrador.imagen_admin()
    return render(request, 'usuarios/usuarios.html', {
        'lista_empleados':lista_empleados,
        'lista_administradores':lista_administradores,
        'form_empleados': form_empleados,
        'form_administradores': form_administradores,
        'imagen_administrador': imagen_administrador,
        })

def acceder_administrador(request):
    if request.method == "POST":
        form = AccederUsuarioForm(request.POST)
        if form.is_valid():
            # Traemos el correo y la contraseña proporcionada por el usuario
            correo = form.cleaned_data['correo']
            contraseña = form.cleaned_data['contraseña']
            
            # Traemos a todos los clientes de la base de datos
            usuario_ref = db.collection('restaurante1').document('usuarios').collection('administradores')
            # Verificamos que el correo que proporciono el usuario exista
            query = usuario_ref.where("correo", "==", correo).get()
            
            # Si el correo existe se cumple esta condificon
            if query:
                # Traemos los datos del usuario con base al correo
                cliente = query[0].to_dict()
                # Guardamos la contraseña del usuario en una variable para compararla
                contraseña_encriptada = cliente['contraseña']
                # Verificamos ambas contraseñas, tanto la encriptada como la proporicionada por el usuario, esta ultima se encripta para que coincida con la guardada en la base de datos
                if bcrypt.checkpw(contraseña.encode(), contraseña_encriptada.encode()): #contraseña_encriptada.encode(): esto convierte la contraseña encriptada (que fue almacenada en la base de datos) en bytes para que bcrypt pueda realizar la comparación.
                    return redirect('admin')
                else:
                    form.add_error(None, "La contraseña es incorrecta")
            # Si no existe se cumple el else
            else:
                form.add_error(None, "No se encontró un usuario con este correo")
    else:
        form = AccederUsuarioForm()
    return render(request, "administradores/acceder_administradores.html", {'form': form})