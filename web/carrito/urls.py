from django.urls import path
from . import views

urlpatterns = [
    path('', views.carrito, name= "carrito"),
    path('agregar_producto/<str:producto_id>/<str:origen>/', views.agregar_producto, name = 'agregar_producto'),
]
