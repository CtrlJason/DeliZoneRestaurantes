from django.urls import path
from . import views

urlpatterns = [
    path('', views.seleccionar_tienda, name = "seleccionar_tienda"),
    path('realizar_pago/', views.pasarela_pagos, name = "pasarela_pagos"),
]
