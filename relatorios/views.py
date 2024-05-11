from django.shortcuts import render
from django.http import HttpRequest 
from django.db.models.functions import TruncMonth
from django.db.models import Sum

from recebimento.models import Recebimentos
from .utils.transforms import tableHtmlTransformer
from cliente.models import Cliente

# Create your views here.


def relatorioClienteRecebimentoView(req: HttpRequest):
    
    Recebimento_tabela = Recebimentos.objects.all().values('dataPagamento','cliente').annotate(month=TruncMonth('dataPagamento')).values('month','cliente').annotate(total=Sum('valor')).values('cliente','month','total') 
    
    if req.GET.__len__() == True:
        Recebimento_tabela = Recebimento_tabela.filter(dataPagamento__year=req.GET.get('year'))
        
    context = {}
    
    if Recebimento_tabela and Recebimento_tabela.__len__() > 0:
        
        relatorio, totalRow, total = tableHtmlTransformer(Recebimento_tabela, Cliente).transform()
        
        context = { 'relatorio':relatorio, 'totalMes': totalRow, 'total': total}
      
    return render(req, 'clienteRecebimentoRelatorio.html', context)
