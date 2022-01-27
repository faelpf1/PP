from django.urls import path
from meuOrcamento.views.PerfilView import perfil_view

urlpatterns=[
    path('', perfil_view, name='perfils'),
    path('<int:id>', perfil_view, name='perfil'),    
]

