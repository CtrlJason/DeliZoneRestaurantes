from django.shortcuts import render, redirect
from .forms import RegistroCliente, AccederCliente
from firebase_admin import auth
from firebase import db
import bcrypt

def registro_cliente(request):
    if request.method == "POST":
        form = RegistroCliente(request.POST)
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
                usuario_ref = db.collection('clientes')
                query = usuario_ref.where("email", "==", correo).get()
                if query:
                    form.add_error(None, "El correo ya se encuentra registrado.")
                else:
                    try:
                        db.collection('clientes').add({
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
        form = RegistroCliente()
                
    return render(request, "clientes/registro_cliente.html", {'form': form})

def acceder_cliente(request):
    if request.method == "POST":
        form = AccederCliente(request.POST)
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
        form = AccederCliente()
    return render(request, "clientes/acceder_cliente.html", {'form': form})