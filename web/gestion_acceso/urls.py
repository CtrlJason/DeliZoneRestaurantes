from django.urls import path
from . import views

urlpatterns = [
    path('iniciar_sesion/', views.acceder_cliente, name = 'acceder_cliente'),
    path('registro/', views.registro_cliente, name = 'registro_cliente'),
]
