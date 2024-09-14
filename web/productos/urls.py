from django.urls import path
from . import views

# Static
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.productos, name="productos"),
    path('agregar_productos/', views.agregar_productos, name='agregar_productos'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)