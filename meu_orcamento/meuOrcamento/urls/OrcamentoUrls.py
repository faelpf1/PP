from django.urls import path
from meuOrcamento.views.OrcamentoView import OrcamentoCreateView, OrcamentoListView, OrcamentoUpdate, OrcamentoDelete, CategoriaCreateView

urlpatterns=[
    path('', OrcamentoListView.as_view(), name='orcamento'),
    path('adicionarCategoria/', CategoriaCreateView.as_view(), name='adicionarCategoria'),
    path('adicionarOrcamento/', OrcamentoCreateView.as_view(), name='adicionarOrcamento'),
    path('editarOrcamento/<int:pk>', OrcamentoUpdate.as_view(), name='editarOrcamento'),
    path('excluirOrcamento/<int:pk>', OrcamentoDelete.as_view(), name='excluirOrcamento'),
]