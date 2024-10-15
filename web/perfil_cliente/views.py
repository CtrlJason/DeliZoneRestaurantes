from django.shortcuts import render, redirect
from .forms import CambiarImagenUsuarioForm, CambiarDatosUsuarioForm, CambiarPasswordUsuarioForm
# from .datos_usuario import ver_informacion
from firebase import db, bucket
import bcrypt

# Create your views here.

def perfil_usuario(request):
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
        
        return render(request, "perfil_usuario.html", context)
    
def subir_imagen(image):
    blob = bucket.blob(f"restaurante1/clientes/{image.name}")
    blob.upload_from_file(image, content_type=image.content_type)
    blob.make_public()
    return blob.public_url
    
def actualizar_imagen_usuario(request):
    if request.method == 'POST':
        form = CambiarImagenUsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            imagen = request.FILES.get('imagen')
            # Verificamos si el usuario puso una imagen
            if imagen:
                imagen_url = subir_imagen(imagen)
                cliente_id = request.session['clientes_id']
                cliente_ref = db.collection('restaurante1').document('usuarios').collection('clientes').document(cliente_id)
                cliente_ref.update({
                    'imagen': imagen_url
                })
            else:
                print("No se ha subido ninguna imagen.")
    else:
        form = CambiarImagenUsuarioForm()
    return redirect('perfil_usuario')

def actualizar_perfil_usuario(request):
    if request.method == "POST":
        cliente_id = request.session['clientes_id']
        cliente_ref = db.collection('restaurante1').document('usuarios').collection('clientes').document(cliente_id)
        
        # Actualizamos datos personales
        cliente_ref.update({
            'nombres': request.POST.get('nombres'),
            'apellidos': request.POST.get('apellidos'),
            'celular': request.POST.get('celular'),
            'correo': request.POST.get('correo'),
        })
        
        return redirect('perfil_usuario')
    return redirect('perfil_usuario')

def actualizar_password_usuario(request):
    if request.method == "POST":
        form = CambiarPasswordUsuarioForm(request.POST)
        if form.is_valid():
            cliente_id = request.session['clientes_id']
            cliente_ref = db.collection('restaurante1').document('usuarios').collection('clientes').document(cliente_id)
            
            password_actual = form.cleaned_data["password_actual"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            
            # Obtenermos la contraseña actual encriptada de la base de datos
            password_encriptado = cliente_ref.get().to_dict().get('password')
            
            # verificamos que la contraseña que proporciona el usuario sea la misma que en la base de datos
            if bcrypt.checkpw(password_actual.encode(), password_encriptado.encode()):
                # Verificamos que las contraseñas sean iguales
                if password1 != password2:
                    form.add_error("password2", "las contraseñas no coinciden")
                else:
                    # Actaulizamos la contraseña del usuario
                    nuevo_password_encriptado = bcrypt.hashpw(password1.encode(), bcrypt.gensalt()).decode("utf-8")
                    cliente_ref.update({
                        'password': nuevo_password_encriptado
                    })
                    print("contraseña actualizada")
                    return redirect('perfil_usuario')
            else:
                form.add_error("password_actual", "La contraseña no es correcta")
    else:
        form  = CambiarPasswordUsuarioForm()
    return redirect('perfil_usuario')
