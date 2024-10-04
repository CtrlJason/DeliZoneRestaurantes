from django import forms

class RegistroClienteForm(forms.Form):
    nombre = forms.CharField(max_length = 60, required=True)
    apellido = forms.CharField(max_length = 60, required=True)
    correo = forms.EmailField(required=True)
    celular = forms.IntegerField(required=True, widget = forms.TextInput(attrs={'type': 'tel', 'placeholder': 'Tu número de celular'}))
    contraseña1 = forms.CharField(min_length = 8, required=True, label="Contraseña", widget= forms.PasswordInput())
    contraseña2 = forms.CharField(min_length = 8, required=True, label="Repetir Contraseña", widget= forms.PasswordInput())

class AccederClienteForm(forms.Form):
    correo = forms.EmailField(required=True)
    contraseña = forms.CharField(min_length = 8, required=True, widget= forms.PasswordInput())
    
class RegistroEmpleadoForm(forms.Form):
    nombre = forms.CharField(max_length = 60, required=True)
    apellido = forms.CharField(max_length = 60, required=True)
    correo = forms.EmailField(required=True)
    contraseña = forms.CharField(min_length = 8, required=True, label="Contraseña", widget= forms.PasswordInput())
    cargo = forms.CharField(max_length = 60, required=False)
    