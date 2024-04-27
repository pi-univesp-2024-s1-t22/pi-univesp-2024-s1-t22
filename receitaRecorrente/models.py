from django.db import models
from cliente.models import Cliente
from django.core.validators import MinValueValidator, MaxValueValidator

class ReceitaRecorrente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    diaPagamento = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(28)], null=False, blank=False)
    status = models.BooleanField(null=False, default=True)
    class Meta:
        verbose_name_plural = 'ReceitasRecorrentes'