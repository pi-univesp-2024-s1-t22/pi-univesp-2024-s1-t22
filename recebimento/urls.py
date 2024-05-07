from django.urls import path
from django.contrib.auth.decorators import login_required

from recebimento.views import cadastroRecebimentoView, listaRecebimentoView

urlpatterns = [
    path('newRecebimento/', login_required(cadastroRecebimentoView), name='newrecebimento'),
    path('recebimentos/', login_required(listaRecebimentoView), name='recebimentos'),
]