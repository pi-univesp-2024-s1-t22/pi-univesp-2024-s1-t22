from collections import defaultdict   
from django.db.models import Model

import locale
from functools import reduce


class tableHtmlTransformer:
    
    meses = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
    
    def __init__(self, data, cli_model):
        
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        
        self.tmp: dict = data.values()
        self.cli: Model = cli_model
    
    def transform(self):
        
        result = defaultdict(lambda: defaultdict(float))
        
        for cliente in self.tmp:
            
            mes = cliente.get('month').strftime('%b')
            cli = self.cli.objects.get(id=cliente.get('cliente_id')).nomeCliente
            result[cli][mes] += float(cliente.get('total'))
            
        
        
        totalmes = { mes: 0.0 for mes in self.meses}
        for cliente in list(result.keys()):
                
            tmp = 0.0
            
            for mes in self.meses:
                
                tmp += result[cliente].get(mes, 0.0)
                result[cliente][mes] = result[cliente].get(mes, 0.0)
                totalmes[mes] += result[cliente].get(mes, 0.0)
                
            
            result[cliente]['total'] = tmp  
                
        result = {k: {mes: dict(v).get(mes, 0.0) for mes in [*self.meses,'total']} for k , v in result.items()}
        
        total = reduce(lambda sum, x: sum + x, totalmes.values())
        
        return result, totalmes, total
                     
        