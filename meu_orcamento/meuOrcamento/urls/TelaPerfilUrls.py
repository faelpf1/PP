from django.urls import path
from meuOrcamento.views.TelaPerfilView import tela_perfil_view

urlpatterns=[
    path('', tela_perfil_view, name='perfils'),
    path('<int:id>', tela_perfil_view, name='perfil')
]