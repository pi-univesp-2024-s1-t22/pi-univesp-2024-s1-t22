from django.db import models

class Cliente(models.Model):
    nomeCliente = models.CharField(max_length=100, null=False, blank=False, unique=True)
    class Meta:
        verbose_name_plural = 'Clientes'