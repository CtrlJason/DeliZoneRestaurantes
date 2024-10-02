from django.urls import path
from gestion_contacto import views

urlpatterns = [
    path('', views.gestion_contacto, name = "gestion_contacto"),
    path('eliminar_formulario/<str:formulario_id>/', views.eliminar_formulario, name = "eliminar_formulario"),
]
