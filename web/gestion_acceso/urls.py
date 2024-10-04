from django.urls import path
from . import views

urlpatterns = [
    # --== Clientes ==--
    path('iniciar_sesion/', views.acceder_cliente, name = 'acceder_cliente'),
    path('registro/', views.registro_cliente, name = 'registro_cliente'),
    # --== Usuarios ==-- #
    path('usuarios/', views.ver_usuarios, name = 'ver_usuarios'),
    # --== Registro Empleados ==-- #
    path('registro_empleado/', views.registro_empleado, name = 'registro_empleado'),
    # --== Registro Administradores ==--
    path('registro_administrador/', views.registro_administrador, name = 'registro_administrador'),
]
