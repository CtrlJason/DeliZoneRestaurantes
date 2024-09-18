from django.urls import path
from login import views

urlpatterns = [
    path('', views.login, name='login'),
    path('autenticar_usuario/', views.autenticar_usuario, name="autenticar_usuario"),
    path('register/', views.register, name='register'),
    path('registrar_usuario/', views.registrar_usuario, name='registrar_usuario'),
    # Otras URLs
]
