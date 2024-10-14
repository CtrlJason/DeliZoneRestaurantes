from django.urls import path
from ubicacion import views

urlpatterns = [
    path('', views.ubicacion, name= "ubicacion")
]
