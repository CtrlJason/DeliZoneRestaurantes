from django.urls import path
from . import views

urlpatterns = [
    path("", views.configuracion_sitio, name="configuracion_sitio"),
    path("actualizar_fav_icon/", views.actualizar_fav_icon, name="actualizar_fav_icon"),
    path("actualizar_logo/", views.actualizar_logo, name="actualizar_logo"),
    path("actualizar_colores/", views.actualizar_colores, name="actualizar_colores"),
]
