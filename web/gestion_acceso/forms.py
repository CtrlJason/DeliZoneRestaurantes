from django import forms

class AccederUsuarioForm(forms.Form):
    correo = forms.EmailField(required=True)
    password = forms.CharField(required=True, widget= forms.PasswordInput())

class RegistroClienteForm(forms.Form):
    nombres = forms.CharField(max_length = 30, required=True)
    apellidos = forms.CharField(max_length = 30, required=True)
    correo = forms.EmailField(max_length = 30, required=True)
    celular = forms.IntegerField(required=True, widget = forms.TextInput(attrs={'type': 'tel', 'placeholder': 'Tu número de celular'}))
    password1 = forms.CharField(min_length = 8, required=True, label="Contraseña", widget= forms.PasswordInput())
    password2 = forms.CharField(min_length = 8, required=True, label="Repetir Contraseña", widget= forms.PasswordInput())
    
class RegistroEmpleadoForm(forms.Form):
    nombres = forms.CharField(max_length = 30, required=True)
    apellidos = forms.CharField(max_length = 30, required=True)
    correo = forms.EmailField(max_length = 30, required=True)
    password = forms.CharField(min_length = 8, required=True, label="Contraseña", widget= forms.PasswordInput())
    cargo = forms.CharField(max_length = 60, required=False)
    imagen = forms.ImageField(required = False)

class RegistroAdministradoresForm(forms.Form):
    nombres = forms.CharField(max_length = 30, required=True)
    apellidos = forms.CharField(max_length = 30, required=True)
    correo = forms.EmailField(max_length = 30, required=True)
    password = forms.CharField(min_length = 8, required=True, label="Contraseña", widget= forms.PasswordInput())
    imagen = forms.ImageField(required = False)