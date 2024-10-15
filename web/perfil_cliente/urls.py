from django.urls import path
from . import views

urlpatterns = [
    path('', views.perfil_usuario, name="perfil_usuario"),
    path('actualizar_perfil_usuario/', views.actualizar_perfil_usuario, name = 'actualizar_perfil_usuario'),
    path('actualizar_password_usuario', views.actualizar_password_usuario, name = 'actualizar_password_usuario'),
    path('actualizar_imagen_usuario', views.actualizar_imagen_usuario, name = 'actualizar_imagen_usuario'),
]
