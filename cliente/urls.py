from django.urls import path
from cliente.views import cadastroClienteView, listaClienteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('newCliente/', login_required(cadastroClienteView), name='newcliente'),
    path('clientes/', login_required(listaClienteView), name='clientes')
]

