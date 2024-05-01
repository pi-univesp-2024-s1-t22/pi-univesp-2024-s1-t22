from django import forms
from cliente.models import Cliente

class clienteForm(forms.ModelForm):

    class Meta:

        model = Cliente
        fields = ["nomeCliente"]