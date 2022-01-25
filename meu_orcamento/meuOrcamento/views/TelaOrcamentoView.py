from django.http import HttpResponse
from meuOrcamento.models import Orcamento

def tela_orcamento_view(request):
    categoria = request.GET.get('categoria')
    nome = request.GET.get('nome')
    tipo_orcamento = request.GET.get('tipo_orcamento')
    valor = request.GET.get('valor')
    data = request.GET.get('data')

    orcamentos = Orcamento.objects.all()
    print(orcamentos)

    return HttpResponse("<h1>tela orcamento</h1>")