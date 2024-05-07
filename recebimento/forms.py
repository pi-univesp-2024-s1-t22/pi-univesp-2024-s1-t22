from django import forms 

from cliente.models import Cliente
from recebimento.models import Recebimentos

class RecebimentoForm(forms.ModelForm):
    
    SELECAO_VAZIA = 'Selecione o cliente'
    
    choices = [ (c.id, c.nomeCliente) for c in Cliente.objects.all().order_by("id").reverse() ]  
    
    choices.append((None, SELECAO_VAZIA))
    
    cli = forms.ChoiceField(choices=choices, required=True, initial=(None, SELECAO_VAZIA), label="Cliente")
    
    class Meta:
        
        model = Recebimentos
        fields = ['cli','descricao','valor','dataPagamento']
        
    def save(self, commit=True):
        
        instancia = super(RecebimentoForm, self).save(commit=False)
        instancia.cliente = Cliente.objects.get(id=self.cleaned_data.get('cli'))

        if commit:
            return super().save()
        
        return instancia
            
        
    
    