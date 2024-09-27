from django.urls import path
from . import views

urlpatterns = [
    path('', views.carrito, name= "carrito"),
    path('agregar_producto/<str:producto_id>/', views.agregar_producto, name = 'agregar_producto'),
]
