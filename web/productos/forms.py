from django import forms

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length = 120)
    precio = forms.IntegerField()
    stock = forms.IntegerField()
    imagen = forms.ImageField()
    descripcion = forms.CharField(widget = forms.Textarea, max_length = 160)
