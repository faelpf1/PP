from django.urls import path
from meuOrcamento.views.TelaOrcamentoView import tela_orcamento_view

urlpatterns=[
    path('', tela_orcamento_view, name='orcamentos'),
]