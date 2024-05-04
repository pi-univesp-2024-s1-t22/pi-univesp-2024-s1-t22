from django.urls import path
from despesa.views import cadastroDespesaView, listaDespesaView

urlpatterns = [
    path('newDespesa/', cadastroDespesaView, name='newdespesa'),
    path('despesas/', listaDespesaView, name='despesas')
]