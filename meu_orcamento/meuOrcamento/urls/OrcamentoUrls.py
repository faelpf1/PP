from django.urls import path
from meuOrcamento.views.OrcamentoView import orcamento_view, adicionarOrcamento
from meuOrcamento.views.CategoriaView import adicionarCategoria

urlpatterns=[
    path('', orcamento_view, name='orcamento'),
    path('adicionarCategoria/', adicionarCategoria, name='adicionarCategoria'),
    path('adicionarOrcamento/', adicionarOrcamento, name='adicionarOrcamento'),
]