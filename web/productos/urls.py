from django.urls import path
from . import views

# Static
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.productos, name="productos"),
    path('agregar_productos/', views.agregar_productos, name='agregar_productos'),
    # urls para eliminar o modificar productos
    # Para darle un parametro a un url que va a enviar posterior mente a una funcion de la vista se escribe la direccion con el paramentro 'direccion/<str:parametro>'
    # Nota: el parametro debe de ser el mismo en la funcion y el <> se usa para capturar valores dinamicos en urls y <str <-- Este es el tipo que se desea capturar>
    path('eliminar_producto/<str:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('editar_producto/<str:producto_id>/', views.editar_producto, name='editar_producto'),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)