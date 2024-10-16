from django import forms

class CambiarColoresSitioForm(forms.Form):
    color1 = forms.CharField(max_length = 7, required=True)
    color2 = forms.CharField(max_length = 7, required=True)
    color3 = forms.CharField(max_length = 7, required=True)
    colorbordeboton = forms.CharField(max_length = 7, required=True)
    colorboton1 = forms.CharField(max_length = 7, required=True)
    colorboton2 = forms.CharField(max_length = 7, required=True)
    
class CambiarLogoSitioForm(forms.Form):
    logo = forms.ImageField(required = True)
    
class CambiarFavIconSitioForm(forms.Form):
    fav_icon = forms.ImageField(required = True)