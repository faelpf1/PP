from django.urls import path
from meuOrcamento.views.AutenticacaoView import login_view, register_view, logout_view

urlpatterns = [
    path("", login_view, name='login'),
    path("register", register_view, name='register'),
    path("logout", logout_view, name='logout'), 
]
