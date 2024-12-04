from django import forms

class PedidoForm(forms.Form):
    cliente_id = forms.IntegerField()
    datos_pedido = forms.JSONField()
    productos = forms.JSONField()
    direccion = forms.JSONField()