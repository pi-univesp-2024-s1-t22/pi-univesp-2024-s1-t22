from django.shortcuts import render, redirect
from django.http import HttpRequest

from despesa.forms import DespesaForm

from django.contrib import messages
from django.urls import reverse

from despesa.models import Despesa

# Create your views here.

def cadastroDespesaView(req: HttpRequest):
    
    if req.method == 'POST':
        
        form = DespesaForm(req.POST)
        
        if form.is_valid():
            
            try:
                form.save()
                messages.success(req, 'Despesa criada com sucesso')
                return redirect(reverse('despesas'))
            
            except Exception as e:
                messages.error(req, 'Erro Desconhecido')
        else:
            for e in form.errors:
                print(e)
            messages.error(req, 'Erro ao criar a despesa')        
        
    
    
    context = { 'form': DespesaForm() }
    
    return render(req, 'cadastroDespesa.html', context)


def listaDespesaView(req: HttpRequest):
    
    despesas = Despesa.objects.all().reverse()
    
    context = { 'despesas': despesas}
    
    return render(req, 'listaDespesa.html', context)