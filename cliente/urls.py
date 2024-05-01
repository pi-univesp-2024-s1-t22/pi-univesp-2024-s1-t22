from django.urls import path
from cliente.views import cadastroClienteView, listaClienteView

urlpatterns = [
    path('newCliente/', cadastroClienteView, name='newcliente'),
    path('clientes/', listaClienteView, name='clientes')
]

