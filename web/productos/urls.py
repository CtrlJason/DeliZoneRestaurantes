from django.urls import path
from . import views

urlpatterns = [
    path('', views.productos, name='productos'),
    path('agregar_producto/', views.agregar_producto, name = 'agregar_producto'),
    path('eliminar_producto/<str:producto_id>/', views.eliminar_producto, name = 'eliminar_producto'),
]