from django.urls import path
from . import views

urlpatterns = [
    path('', views.perfil_user, name="perfil_user")
]
