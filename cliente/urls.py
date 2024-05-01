from django.urls import path
from cliente.views import cadastroClienteView, listaClienteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('newCliente/', login_required(cadastroClienteView), name='newcliente'),
    path('clientes/', login_required(listaClienteView), name='clientes'),
    path('login/', LoginView.as_view(template_name='admin/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

