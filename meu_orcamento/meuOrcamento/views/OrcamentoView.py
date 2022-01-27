from meuOrcamento.models import Orcamento
from django.shortcuts import render
from meuOrcamento.forms.OrcamentoForm import OrcamentoForm

def orcamento_view(request):
    categoria = request.GET.get('categoria')
    nome = request.GET.get('nome')
    tipo_orcamento = request.GET.get('tipo_orcamento')
    valor = request.GET.get('valor')
    data = request.GET.get('data')

    orcamentos = Orcamento.objects.all()
    print(orcamentos)

    context = {
        
    }

    return render(request, template_name='orcamento.html', context=context)


def adicionarOrcamento(request):
    message = None
    if request.method == 'POST':
        orcamento = OrcamentoForm(request.POST)
        if orcamento.is_valid():
            orcamento.save()
            if orcamento is not None:
                message = { 'type': 'success', 'text': 'Orçamento adicionado com sucesso!' }
            else:
                message = { 'type': 'danger',  'text': 'Um erro ocorreu.' }
            nome = orcamento.cleaned_data['nome']
            valor = orcamento.cleaned_data['valor']

    context = {
        'form': OrcamentoForm(),
        'message': message,
        'title': 'Adicionar Orçamento',
        'button_text': 'Adicionar Orçamento',
        'link_text': 'Voltar',
        'link_href': '/orcamento'
    }
    
    return render(request, 'adicionarOrcamento.html', context=context)