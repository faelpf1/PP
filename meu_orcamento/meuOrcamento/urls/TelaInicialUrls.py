from django.urls import path
from meuOrcamento.views.TelaInicialView import tela_inicial_view

urlpatterns=[
    path('', tela_inicial_view),
]