from django.views.generic import DetailView, ListView
from .models import Orcamento
from .forms import adicionarCategoriaForm, adicionarOrcamentoForm
from django.shortcuts import render

class OrcamentoListView( ListView ):
    model = Orcamento

class OrcamentoDetailView( DetailView ):
    model = Orcamento


def adicionarCategoria(request):
    if request.method == 'POST':
        form = adicionarCategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            nome = form.cleaned_data['nome']
            descricao = form.cleaned_data['descricao']
    form = adicionarCategoriaForm()
    return render(request, 'conta/adicionarCategoria.html', {'form': form})

def adicionarOrcamento(request):
    if request.method == 'POST':
        form = adicionarOrcamentoForm(request.POST)
        if form.is_valid():
            form.save()
            nome = form.cleaned_data['nome']
            valor = form.cleaned_data['valor']
            data = form.cleaned_data['data']
    form = adicionarOrcamentoForm()
    return render(request, 'conta/adicionarOrcamento.html', {'form': form})