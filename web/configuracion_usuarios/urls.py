from django.urls import path
from . import views

urlpatterns = [
    path('usuario/', views.perfil_cliente, name="perfil_clientes"),
    path('admin/', views.perfil_administrador, name="perfil_administradores"),
    path('actualizar_perfil_usuario/<str:rol>/', views.actualizar_perfil_usuario, name = 'actualizar_perfil_usuario'),
    path('actualizar_password_usuario/<str:rol>/', views.actualizar_password_usuario, name = 'actualizar_password_usuario'),
    path('actualizar_imagen_usuario/<str:rol>/', views.actualizar_imagen_usuario, name = 'actualizar_imagen_usuario'),
]