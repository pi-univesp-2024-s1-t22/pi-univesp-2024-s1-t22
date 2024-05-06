from django import forms 

from despesa.models import Despesa, TipoDespesa

class DespesaForm(forms.ModelForm):
    
    choices = [ (tipo.id, tipo.tipo) for tipo in TipoDespesa.objects.all()]  
    
    choices.append((None, 'selecione tipo'))
    
    tipo = forms.ChoiceField(choices=choices, required=True, initial=(None, 'selecione tipo'), label="Tipo Despesa")
    
    
    class Meta:
        
        model = Despesa
        fields = ['tipo','valor','dataPagamento','descricao']
        
    def save(self, commit=True):
        
        instancia = super(DespesaForm, self).save(commit=False)
        instancia.tipoDespesa = TipoDespesa.objects.get(id=self.cleaned_data.get('tipo'))

        if commit:
            return super().save()
        
        return instancia
            
        
    
    