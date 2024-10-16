from django.shortcuts import render, redirect
from .forms import CambiarImagenUsuarioForm, CambiarDatosUsuarioForm, CambiarPasswordUsuarioForm
# from .datos_usuario import ver_informacion
from firebase import db, bucket
import bcrypt

# Create your views here.

def perfil_cliente(request):
    if 'clientes_id' not in request.session:
        return redirect('acceder_cliente')
    else:
        
        imagen = CambiarImagenUsuarioForm()
        
        cliente_id = request.session['clientes_id']
        cliente_ref = db.collection('restaurante1').document('usuarios').collection('clientes').document(cliente_id).get().to_dict() # to.dict transforma los datos a diccionario
        datos_personales = CambiarDatosUsuarioForm(initial={
            'nombres': cliente_ref.get('nombres'),
            'apellidos': cliente_ref.get('apellidos'),
            'celular': cliente_ref.get('celular'),
            'correo': cliente_ref.get('correo'),
        })
        
        password_usuario = CambiarPasswordUsuarioForm()
        context = {
            "imagen": imagen,
            "datos_personales": datos_personales,
            "contrasenia_usuario": password_usuario,
        }
        
        return render(request, "perfil_clientes.html", context)
    
def perfil_administrador(request):
    if 'administradores_id' not in request.session:
        return redirect('acceder_administrador')
    else:
        
        imagen = CambiarImagenUsuarioForm()
        
        administrador_id = request.session['administradores_id']
        cliente_ref = db.collection('restaurante1').document('usuarios').collection('administradores').document(administrador_id).get().to_dict() # to.dict transforma los datos a diccionario
        datos_personales = CambiarDatosUsuarioForm(initial={
            'nombres': cliente_ref.get('nombres'),
            'apellidos': cliente_ref.get('apellidos'),
            'celular': cliente_ref.get('celular'),
            'correo': cliente_ref.get('correo'),
        })
        
        password_usuario = CambiarPasswordUsuarioForm()
        context = {
            "imagen": imagen,
            "datos_personales": datos_personales,
            "contrasenia_admin": password_usuario,
        }
        
        return render(request, "perfil_administradores.html", context)
    
def subir_imagen(image, rol):
    blob = bucket.blob(f"restaurante1/{rol}/{image.name}")
    blob.upload_from_file(image, content_type=image.content_type)
    blob.make_public()
    return blob.public_url
    
def actualizar_imagen_usuario(request, rol):
    if request.method == 'POST':
        form = CambiarImagenUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            imagen = request.FILES.get('imagen')
            # Verificamos si el usuario puso una imagen
            if imagen:
                imagen_url = subir_imagen(imagen)
                usuario_id = request.session[f'{rol}_id']
                usuario_ref = db.collection('restaurante1').document('usuarios').collection(rol).document(usuario_id)
                # Borramos la imagen anterior
                # ------ #
                usuario_ref.update({
                    'imagen': imagen_url
                })
            else:
                print("No se ha subido ninguna imagen.")
    else:
        form = CambiarImagenUsuarioForm()
    return redirect(f'perfil_{rol}')

def actualizar_perfil_usuario(request, rol):
    if request.method == "POST":
        usuario_id = request.session[f'{rol}_id']
        usuario_ref = db.collection('restaurante1').document('usuarios').collection(rol).document(usuario_id)
        
        # Actualizamos datos personales
        usuario_ref.update({
            'nombres': request.POST.get('nombres'),
            'apellidos': request.POST.get('apellidos'),
            'celular': request.POST.get('celular'),
            'correo': request.POST.get('correo'),
        })
        
        return redirect(f'perfil_{rol}')
    return redirect(f'perfil_{rol}')

def actualizar_password_usuario(request, rol):
    if request.method == "POST":
        form = CambiarPasswordUsuarioForm(request.POST)
        if form.is_valid():
            usuario_id = request.session[f'{rol}_id']
            usuario_ref = db.collection('restaurante1').document('usuarios').collection(rol).document(usuario_id)
            
            password_actual = form.cleaned_data["password_actual"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            
            # Obtenermos la contraseña actual encriptada de la base de datos
            password_encriptado = usuario_ref.get().to_dict().get('password')
            
            # verificamos que la contraseña que proporciona el usuario sea la misma que en la base de datos
            if bcrypt.checkpw(password_actual.encode(), password_encriptado.encode()):
                # Verificamos que las contraseñas sean iguales
                if password1 != password2:
                    form.add_error("password2", "las contraseñas no coinciden")
                else:
                    # Actaulizamos la contraseña del usuario
                    nuevo_password_encriptado = bcrypt.hashpw(password1.encode(), bcrypt.gensalt()).decode("utf-8")
                    usuario_ref.update({
                        'password': nuevo_password_encriptado
                    })
                    print("contraseña actualizada")
                    return redirect(f'perfil_{rol}')
            else:
                form.add_error("password_actual", "La contraseña no es correcta")
    else:
        form  = CambiarPasswordUsuarioForm()
    return redirect(f'perfil_{rol}')