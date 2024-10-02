from django.urls import path
from contacto import views

urlpatterns = [
    path('', views.contacto, name="contacto"),
    path('crear_contacto/',views.crear_contacto, name="crear_contacto"),
]