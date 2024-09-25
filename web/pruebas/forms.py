from django import forms

class PruebaForm(forms.Form):
    nombre = forms.CharField(max_length = 20)
    celular = forms.IntegerField(max_value = 10)
    correo = forms.EmailField(required = True)
    contraseña = forms.PasswordInput()