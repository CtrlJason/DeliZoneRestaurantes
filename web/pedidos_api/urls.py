from django.urls import path
from .views import PedidoApiView

urlpatterns = [
    path('pedidos/', PedidoApiView.as_view(), name='pedidos_api'),
]