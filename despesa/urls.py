from django.urls import path
from despesa.views import cadastroDespesaView, listaDespesaView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('newDespesa/', login_required(cadastroDespesaView), name='newdespesa'),
    path('despesas/', login_required(listaDespesaView), name='despesas'),
]