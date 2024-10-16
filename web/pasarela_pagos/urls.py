from django.urls import path
from . import views

urlpatterns = [
    path('', views.seleccionar_tienda, name = "seleccionar_tienda"),
    path('pasarela_pagos/', views.pasarela_pagos, name = "pasarela_pagos"),
    path('realizar_pago/', views.realizar_pago, name = "realizar_pago"),
]
