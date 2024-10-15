from django import forms

class CambiarImagenUsuarioForm(forms.Form):
    imagen = forms.ImageField(required=True)

class CambiarDatosUsuarioForm(forms.Form):
    nombres = forms.CharField(required=True, error_messages={'required': 'Por favor, ingrese su nombre.'})
    apellidos = forms.CharField(required=True, error_messages={'required': 'Por favor, ingrese su apellido.'})
    celular = forms.IntegerField(required=False)
    correo = forms.EmailField(required=True, error_messages={'required': 'Por favor, ingrese su correo electronico.'})
    
class CambiarPasswordUsuarioForm(forms.Form):
    password_actual = forms.CharField(widget=forms.PasswordInput, label='Contraseña actual')
    password1 = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirmar contraseña')