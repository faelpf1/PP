from meuOrcamento.models import Orcamento, Categoria
from meuOrcamento.forms.OrcamentoForm import OrcamentoForm
from meuOrcamento.forms.CategoriaForm import CategoriaForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

class PassRequestToFormViewMixin:
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class OrcamentoListView( ListView ):
    model = Orcamento
    template_name='Orcamento/orcamento.html'
    def get_queryset(self):
        return Orcamento.objects.filter(id_user=self.request.user.id)


class CategoriaCreateView( CreateView ):
    model = Categoria
    form_class = CategoriaForm
    template_name='Orcamento/adicionarCategoria.html'
    success_url = reverse_lazy('orcamento')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.id_user = self.request.user
        self.object.save()
        return super().form_valid(form)


class OrcamentoCreateView( PassRequestToFormViewMixin, CreateView ):
    model = Orcamento
    form_class = OrcamentoForm
    template_name='Orcamento/adicionarOrcamento.html'
    success_url = reverse_lazy('orcamento')

    '''def get(self, request, *args, **kwargs):
        filtro = Orcamento.objects.filter(categoria__id_user=self.request.user.id)
        form = self.form_class(initial=self.initial)
        
        return render(request, self.template_name, {'form': form})'''

    def form_valid(self, form):
        form.instance.categoria__id_user = self.request.user.id
        self.object = form.save(commit=False)
        self.object.id_user = self.request.user
        self.object.save()
        return super().form_valid(form)


class OrcamentoUpdate(UpdateView):
    model = Orcamento
    form_class = OrcamentoForm
    template_name = 'Orcamento/editarOrcamento.html'
    success_url = reverse_lazy('orcamento')


class OrcamentoDelete(DeleteView):
    model = Orcamento
    template_name = 'Orcamento/excluirOrcamento.html'
    success_url = reverse_lazy('orcamento')




'''def adicionarOrcamento( request ):
    message = None
    if request.method == 'POST':
        orcamento = OrcamentoForm( request.POST )
        if orcamento.is_valid():
            obj = orcamento.save( commit = False )
            obj.id_user = request.user
            obj.save()
            if orcamento is not None:
                message = { 'type': 'success', 'text': 'Orçamento adicionado com sucesso!' }
            else:
                message = { 'type': 'danger',  'text': 'Erro ao adicionar o orçamento.' }
            #nome = orcamento.cleaned_data['nome']
            #valor = orcamento.cleaned_data['valor']
    context = {
        'form': OrcamentoForm(),
        'message': message,
        'title': 'Adicionar Orçamento',
        'button_text': 'Adicionar Orçamento',
        'link_text': 'Voltar',
        'link_href': '/orcamento'
    }
    return render( request, template_name = 'Orcamento/adicionarOrcamento.html', context = context, status = 200 )'''

    
'''def editar_orcamento( request, id ):
    orcamento = get_object_or_404( Orcamento, id=id )
    orcamentoForm = OrcamentoForm( instance = orcamento ) 

    message = None
    if orcamentoForm.is_valid():
        orcamentoForm.save()
        message = { 'type': 'sucess', 'text': 'Orçamento atualizado com sucesso!' }
    else:
        message = { 'type': 'danger', 'text': 'Erro ao atualizar o orçamento.' }
    context = {
        'orcamentoForm': orcamentoForm,
        'message': message,
        'title': 'Atualizar Orçamento',
        'button_text': 'Salvar',
        'link_text': 'Voltar',
        'link_href': '/orcamento'
    }
    return render( request, template_name = 'Orcamento/editarOrcamento.html', context = context, status = 200 )'''


'''def orcamento_view( request ):
    orcamentos = Orcamento.objects.filter(id_user=request.user.id)
    context = {
        'orcamentos' : orcamentos,
        'title': 'Orçamentos',
    }

    return render( request, template_name='Orcamento/orcamento.html', context = context, status = 200 ) '''   

'''
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
    
    return render(request, 'Orcamento/adicionarCategoria.html', context=context)'''