from django.db import models



class TipoDespesa(models.Model):
    
    tipo = models.CharField(max_length=40, null=False, blank=False)
    
    class Meta:
        
        verbose_name_plural = 'Despesas'


class Despesa(models.Model):
    
    tipoDespesa = models.ForeignKey(TipoDespesa, on_delete=models.PROTECT)
    descricao = models.TextField(null=False, blank=False)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    dataPagamento = models.DateField(null=False, blank=False)
    class Meta:
        
        verbose_name_plural = 'Despesas'