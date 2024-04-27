from django.db import models
from cliente.models import Cliente

class Recebimentos(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    valor = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank=False)
    dataPagamento = models.DateField(null=False, blank=False)
    class Meta:
        verbose_name_plural = 'Recebimentos'