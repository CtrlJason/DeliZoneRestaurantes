from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock', 'imagen', 'descripcion']
    widgets = {
            'descripcion': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
        }
