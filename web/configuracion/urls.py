from django.urls import path
from . import views

urlpatterns = [
    path(
        "admin/", views.configuracion_administrador, name="configuracion_administrador"
    ),
    path("sitio/", views.configuracion_sitio, name="configuracion_sitio"),
]
