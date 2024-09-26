# importamos la libreria de ModelForms
from django import forms

# Creamos el formulario
class ContactForm(forms.Form):
    nombre = forms.CharField(required=True, max_length = 22)
    celular = forms.IntegerField(required=True)
    correo = forms.EmailField(required=True, max_length = 60)
    asunto = forms.CharField(
        widget = forms.Textarea,
        max_length = 200,
        required = True,
        )