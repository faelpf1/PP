from django.urls import path
from meuOrcamento.views.PerfilView import perfil_view, editar_perfil

urlpatterns=[
    path('', perfil_view, name='perfils'),
    path('<int:id>', perfil_view, name='perfil'),
    path("edit", editar_perfil, name='editarPerfil'),
    
]

