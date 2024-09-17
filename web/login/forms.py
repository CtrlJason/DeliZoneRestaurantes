from django import forms

class RegisterForm(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    correo = forms.EmailField()
    contraseña = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    confirmar_contraseña = forms.CharField(widget=forms.PasswordInput, label="Confirmar contraseña")
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("contraseña")
        confirm_password = cleaned_data.get("confirmar_contraseña")

        if password != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return cleaned_data

class AuthUserForm(forms.Form):
    correo = forms.CharField(label="Correo")
    contraseña = forms.CharField(label="Contraseña")