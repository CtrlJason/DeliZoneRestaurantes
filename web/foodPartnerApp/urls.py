from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # path('add_car/', views.agregar_carrito, name='add_car')
]