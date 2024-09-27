from django.urls import path
from contacto import views

urlpatterns = [
    path('', views.contacto, name="contacto"),
    path('crear_contacto/',views.crear_contacto, name="crear_contacto"),
    path('ver_formularios/', views.ver_formularios, name = "ver_formularios"),
    path('eliminar_formulario/<str:formulario_id>/', views.eliminar_formulario, name = "eliminar_formulario"),
]