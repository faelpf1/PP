from django.urls import path
from meuOrcamento.views.OrcamentoView import orcamento_view

urlpatterns=[
    path('', orcamento_view, name='orcamento'),
]