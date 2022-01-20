from django.urls import path
from . import views

app_name = "conta"

urlpatterns = [
   # path("", views.OrcamentoListView.as_view(), name = "list"),
    path("adicionarCategoria/", views.adicionarCategoria),
    path("adicionarOrcamento/", views.adicionarOrcamento),
]
