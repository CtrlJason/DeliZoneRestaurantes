from django.shortcuts import render, redirect
from .forms import CambiarLogoSitioForm, CambiarFavIconSitioForm, CambiarColoresSitioForm
from firebase import db, bucket

# Create your views here.

def configuracion_sitio(request):
    if 'administradores_id' not in request.session:
        return redirect('acceder_administrador')
    else:
        logo = CambiarLogoSitioForm()
        fav_icon = CambiarFavIconSitioForm()
        sitio_ref = db.collection('restaurante1').document('configuracion').get().to_dict()
        
        if not sitio_ref:
            sitio_ref = db.collection('restaurante1').document('configuracion').set({
                'color1': '#fff',
                'color2': '#042434',
                'color3': '#161A1D',
                'colorbordeboton': '#660708',
                'colorboton1': '#E5383B',
                'colorboton2': '#BA181B',
                'logo': 'https://firebasestorage.googleapis.com/v0/b/delizone-1a227.appspot.com/o/restaurante1%2Fimagenes%2FLocoConTexto.svg?alt=media&token=7a5b0bc9-7360-4d12-815f-cf60031a0ced',
                'fav_icon_sitio': 'https://firebasestorage.googleapis.com/v0/b/delizone-1a227.appspot.com/o/restaurante1%2Fimagenes%2FLogo.svg?alt=media&token=24af3c22-2bb4-4538-ae2c-59b339e23efd',
            })
            colores_sitio = CambiarColoresSitioForm(initial={
                'color1': '#fff',
                'color2': '#042434',
                'color3': '#161A1D',
                'colorbordeboton': '#660708',
                'colorboton1': '#E5383B',
                'colorboton2': '#BA181B',
            })
            context = {
                'logo': logo,
                'fav_icon': fav_icon,
                'colores_sitio': colores_sitio
            }
        else:
            colores_sitio = CambiarColoresSitioForm(initial={
                'color1': sitio_ref.get('color1'),
                'color2': sitio_ref.get('color2'),
                'color3': sitio_ref.get('color3'),
                'colorbordeboton': sitio_ref.get('colorbordeboton'),
                'colorboton1': sitio_ref.get('colorboton1'),
                'colorboton2': sitio_ref.get('colorboton2'),
            })
            context = {
                'logo': logo,
                'fav_icon': fav_icon,
                'colores_sitio': colores_sitio
            }
    
    return render(request, "configuracion_sitio.html", context)

def subir_imagen(image):
    blob = bucket.blob(f"restaurante1/imagenes_sitio/{image.name}")
    blob.upload_from_file(image, content_type=image.content_type)
    blob.make_public()
    return blob.public_url

def actualizar_fav_icon(request):
    if request.method == 'POST':
        form = CambiarFavIconSitioForm(request.POST, request.FILES)
        if form.is_valid:
            icono = request.FILES.get('fav_icon')
            if icono:
                icono_url = subir_imagen(icono)
                db.collection('restaurante1').document('configuracion').update({
                    'fav_icon_sitio': icono_url
                })
            else:
                print("no se pudo actualizar el fav icon")
        else:
            form = CambiarFavIconSitioForm()
        return redirect('configuracion_sitio')

def actualizar_logo(request):
    if request.method == 'POST':
        form = CambiarLogoSitioForm(request.POST, request.FILES)
        if form.is_valid:
            logo = request.FILES.get('logo')
            logo_url = subir_imagen(logo)
            db.collection('restaurante1').document('configuracion').update({
                'logo': logo_url
            })
        else:
            form = CambiarLogoSitioForm()
        return redirect('configuracion_sitio')

def actualizar_colores(request):
    if request.method == 'POST':
        form = CambiarColoresSitioForm(request.POST)
        if form.is_valid:
            db.collection('restaurante1').document('configuracion').update({
                'color1': request.POST.get('color1'),
                'color2': request.POST.get('color2'),
                'color3': request.POST.get('color3'),
                'colorbordeboton': request.POST.get('colorbordeboton'),
                'colorboton1': request.POST.get('colorboton1'),
                'colorboton2': request.POST.get('colorboton2'),
            })
        return redirect('configuracion_sitio')