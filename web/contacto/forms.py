# importamos la libreria de ModelForms
from django import forms
# Importamos los modelos de la app contacto
from .models import DatosUsuarios

# Creamos el formulario
class ContactForm(forms.ModelForm):
    class Meta:
        model = DatosUsuarios
        fields = "__all__"