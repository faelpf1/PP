from django.shortcuts import render
from meuOrcamento.forms.CategoriaForm import CategoriaForm
from meuOrcamento.models.Categoria import Categoria
from django.contrib.auth.models import User


def adicionarCategoria(request):
    message = None
    if request.method == 'POST':
        categoria = CategoriaForm(request.POST)
        if categoria.is_valid():
            obj = categoria.save(commit = False)
            obj.id_user = request.user
            obj.save()
            if categoria is not None:
                message = { 'type': 'success', 'text': 'Categoria adicionada com sucesso!' }
            else:
                message = { 'type': 'danger',  'text': 'Um erro ocorreu.' }
            nome = categoria.cleaned_data['nome']
            descricao = categoria.cleaned_data['descricao']

    context = {
        'form': CategoriaForm(),
        'message': message,
        'title': 'Adicionar Categoria',
        'button_text': 'Adicionar Categoria',
        'link_text': 'Voltar',
        'link_href': '/orcamento'
    }
    
    return render(request, 'Orcamento/adicionarCategoria.html', context=context)