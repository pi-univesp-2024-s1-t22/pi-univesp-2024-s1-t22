from django.shortcuts import render, redirect
from cliente.forms import clienteForm
from django.http import HttpRequest
from cliente.models import Cliente
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def cadastroClienteView(req: HttpRequest):

    if req.method == 'POST':
        form = clienteForm(req.POST)

        if form.is_valid():
            try:
                form.save()
                messages.success(req, 'Cliente criado com sucesso')
                return redirect(reverse('clientes'))
            except Exception as e:
                messages.error(req, 'Erro Desconhecido') 
        else:
            messages.error(req, 'Erro ao criar o cliente') 

    context = {'form': clienteForm()}

    return render(req, 'cadastroCliente.html', context)


def listaClienteView(req: HttpRequest):

    clientes = Cliente.objects.all().reverse()
    context = {'clientes': clientes}

    return render(req, 'listaCliente.html', context)