from django.db import models
from cliente.models import Cliente
from django.core.validators import MinValueValidator

class Recebimentos(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False, validators=[MinValueValidator(0.01)])
    dataPagamento = models.DateField(null=False, blank=False)
    class Meta:
        verbose_name_plural = 'Recebimentos'