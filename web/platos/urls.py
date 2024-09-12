from django.urls import path
from . import views

# Static
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.platos, name="Platos")
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)