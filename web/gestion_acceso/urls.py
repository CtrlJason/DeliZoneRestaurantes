from django.urls import path
from . import views

urlpatterns = [
    # Clientes
    path('iniciar_sesion/', views.acceder_cliente, name = 'acceder_cliente'),
    path('registro/', views.registro_cliente, name = 'registro_cliente'),
    # Empleados
    path('empleados/', views.ver_empleados, name = 'ver_empleados'),
    path('registro_empleados/', views.registro_empleado, name = 'registro_empleados'),
]
