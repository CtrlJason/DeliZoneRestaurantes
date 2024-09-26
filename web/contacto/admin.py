from django.contrib import admin

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display=(
        "id",
        "nombre",
        "imagenCategoria",
        "created",
    )
    search_fields=("nombre", "created")
    list_display=("created",)
    date_hierarchy="created"
    
class ProductoAdmin(admin.ModelAdmin):
    list_display=(
        "id",
        "nombre",
        "imagen",
        "contenido",
        "precio",
        "disponibilidad",
        "created",
    )
    search_fields=("nombre", "contenido", "precio", "created")
    list_filter=("created",)
    date_hierarchy="created"