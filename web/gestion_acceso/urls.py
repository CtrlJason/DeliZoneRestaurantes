from django.urls import path
from . import views

urlpatterns = [
    # --== Acceso ==-- #
    path('iniciar_sesion/', views.acceder_cliente, name = 'acceder_cliente'),
    path('iniciar_sesion_admin/', views.acceder_administrador, name = 'acceder_administrador'),
    # --== Cierre Sesion ==-- #
    path('cierre_sesion_cliente/', views.cerrar_session_cliente, name = 'cerrar_session_cliente'),
    path('cierre_sesion_admin/', views.cerrar_session_administrador, name = 'cerrar_session_administrador'),
    # --== Usuarios ==-- #
    path('usuarios/', views.ver_usuarios, name = 'ver_usuarios'),
    # --== Registro Clientes ==-- #
    path('registro/', views.registro_cliente, name = 'registro_cliente'),
    # --== Registro Empleados ==-- #
    path('registro_empleado/', views.registro_empleado, name = 'registro_empleado'),
    # --== Registro Administradores ==-- #
    path('registro_administrador/', views.registro_administrador, name = 'registro_administrador'),
    # --== Eliminacion Usuarios ==--
    path('eliminar_empleado/<str:id_empleado>/', views.eliminar_empleado, name = 'eliminar_empleado'),
    path('eliminar_administrador/<str:id_administrador>/', views.eliminar_administrador, name = 'eliminar_administrador'),
]
