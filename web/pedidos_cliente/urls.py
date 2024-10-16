from django.urls import path
from . import views

urlpatterns = [
    path('', views.pedidos_cliente, name = 'pedidos_cliente')
]
