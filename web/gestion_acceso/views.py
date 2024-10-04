from django.shortcuts import render, redirect
from .forms import RegistroClienteForm, AccederClienteForm, RegistroEmpleadoForm
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
                            'email': correo,
                            'celular': celular,
                            'contraseña': contraseña_encriptada
                        })
                        return redirect('acceder_cliente')
                    except Exception as e:
                        form.add_error(None, f"Error al registrar el usuario: {e}")
    else:
        form = RegistroClienteForm()
                
    return render(request, "clientes/registro_cliente.html", {'form': form})

def acceder_cliente(request):
    if request.method == "POST":
        form = AccederClienteForm(request.POST)
        if form.is_valid():
            # Traemos el correo y la contraseña proporcionada por el usuario
            correo = form.cleaned_data['correo']
            contraseña = form.cleaned_data['contraseña']
            
            # Traemos a todos los clientes de la base de datos
            usuario_ref = db.collection("clientes")
            # Verificamos que el correo que proporciono el usuario exista
            query = usuario_ref.where("email", "==", correo).get()
            
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
        form = AccederClienteForm()
    return render(request, "clientes/acceder_cliente.html", {'form': form})

# --=================== EMPLEADOS ===================-- #

def ver_empleados(request):
    form = RegistroEmpleadoForm()
    docs = db.collection('restaurante1').document('usuarios').collection('empleados').stream()
    lista_empleados = []
    
    for doc in docs:
        lista_empleados.append(doc.to_dict())
    return render(request, 'empleados/empleados.html', {'lista_empleados': lista_empleados, 'form': form})

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
                        'rol': 'empleado'
                    })
                except Exception as e:
                    form.add_error(None, 'Error al registrar al empleado')
    else:
        form = RegistroEmpleadoForm()
    return render(request, 'empleados/empleados.html', {'form': form})