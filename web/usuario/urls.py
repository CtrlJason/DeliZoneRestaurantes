from django.urls import path
from . import views

# Static
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', views.perfil_user, name="perfil_user")
]
