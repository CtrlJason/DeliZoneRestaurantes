from django.urls import path
from . import views

urlpatterns = [
    path('', views.carrito, name= "carrito"),
    path('agregar_producto/<str:producto_id>/<path:origen>/', views.agregar_producto, name = 'agregar_producto'),
    path('eliminar_producto/<str:producto_id>/<path:origen>/', views.eliminar_producto, name = 'eliminar_producto'),
]
