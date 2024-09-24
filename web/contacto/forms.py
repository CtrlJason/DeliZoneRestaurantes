# importamos la libreria de ModelForms
from django import forms

# Creamos el formulario
class ContactForm(forms.Form):
    nombre = forms.CharField(required=True, max_length = 22)
    celular = forms.IntegerField(required=True, max_value = 10)
    correo = forms.EmailField(required=True, max_length = 60)
    asunto = forms.Textarea()