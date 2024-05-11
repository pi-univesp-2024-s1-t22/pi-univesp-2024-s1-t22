from django.urls import path
from .views import relatorioClienteRecebimentoView

urlpatterns = [
    path('relatorios/cliente-recebimento', relatorioClienteRecebimentoView, name='clienterelatorio'),
]