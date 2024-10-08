from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("admin/", views.home, name="admin"),
    # --== Usuarios ==-- #
    path("admin/usuarios/", views.ver_usuarios, name="ver_usuarios"),
]
