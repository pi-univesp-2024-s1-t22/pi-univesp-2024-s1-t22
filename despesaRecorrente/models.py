from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from despesa.models import TipoDespesa

class DespesaRecorrente(models.Model):
    
    tipoDespesa = models.ForeignKey(TipoDespesa, on_delete=models.PROTECT)
    descricao = models.TextField(null=False, blank=False)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    diaPagamento = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(28)], null=False, blank=False)
    
    class Meta:
        verbose_name_plural = 'Despesas'