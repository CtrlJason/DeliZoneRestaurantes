from django.urls import path
from . import views

urlpatterns = [
    path('', views.pasarela_pagos, name = "pasarela_pagos"),
    path('tienda/', views.escoger_tienda, name = "tienda"),
]
