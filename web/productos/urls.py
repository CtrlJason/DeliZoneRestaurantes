from django.urls import path
from . import views

# Static
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('crear_productos/', views.crear_producto, name='crear_productos'),
    path('productos/', views.productos, name="productos"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)