from django.shortcuts import render, redirect
from django.http import HttpRequest

from django.contrib import messages
from django.urls import reverse

from recebimento.models import Recebimentos
from recebimento.forms import RecebimentoForm

# Create your views here.

def cadastroRecebimentoView(req: HttpRequest):
    
    if req.method == 'POST':
        
        form = RecebimentoForm(req.POST)
        
        if form.is_valid():
            
            try:
                form.save()
                messages.success(req, 'Recebimento criado com sucesso')
                return redirect(reverse('recebimentos'))
            
            except Exception as e:
                messages.error(req, e)
        else:
            print(form.errors)
            for e in form.errors:
                print(e)
            messages.error(req, e)        
        
    
    
    context = { 'form': RecebimentoForm() }
    
    return render(req, 'cadastroRecebimento.html', context)


def listaRecebimentoView(req: HttpRequest):
    
    recebimentos = Recebimentos.objects.all().reverse()
    
    context = { 'recebimentos': recebimentos}
    
    return render(req, 'listaRecebimento.html', context)