from django import forms

class CambiarColoresSitioForm(forms.Form):
    color1 = forms.CharField(label = "Selecciona un color para el menu de navegacion", widget = forms.TextInput(attrs={'type': 'color'}), required=True)
    color2 = forms.CharField(label = "Selecciona un color para el fondo", widget = forms.TextInput(attrs={'type': 'color'}), required=True)
    color3 = forms.CharField(label = "Selecciona un color el pie de pagina", widget = forms.TextInput(attrs={'type': 'color'}), required=True)
    colorbordeboton = forms.CharField(label = "Selecciona un color para el borde de los botones", widget = forms.TextInput(attrs={'type': 'color'}), required=True)
    colorboton1 = forms.CharField(label = "Selecciona un color para el boton", widget = forms.TextInput(attrs={'type': 'color'}), required=True)
    colorboton2 = forms.CharField(label = "Selecciona un color para el boton (presionar)", widget = forms.TextInput(attrs={'type': 'color'}), required=True)
    
class CambiarLogoSitioForm(forms.Form):
    logo = forms.ImageField(required = True)
    
class CambiarFavIconSitioForm(forms.Form):
    fav_icon = forms.ImageField(required = True)