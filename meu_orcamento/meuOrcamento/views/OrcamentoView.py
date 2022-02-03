from django.shortcuts import render
from meuOrcamento.models import Orcamento, Categoria
from meuOrcamento.forms.OrcamentoForm import OrcamentoForm
from meuOrcamento.forms.CategoriaForm import CategoriaForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
import datetime

class PassRequestToFormView:
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class OrcamentoListView( ListView ):
    model = Orcamento
    template_name='Orcamento/orcamento.html'
    def get_context_data(self, **kwargs):
        context = super(OrcamentoListView, self).get_context_data(**kwargs)
        def get_month_year():
            month=datetime.date.today().month
            if(month<10):
                data_atual=str(datetime.date.today().year)+"-0"+str(datetime.date.today().month)
            else:
                data_atual=str(datetime.date.today().year)+"-"+str(datetime.date.today().month)
            return data_atual
        context['data_atual'] = get_month_year()
        return context

    def get_queryset(self):
        orcamento = Orcamento.objects.filter(id_user=self.request.user.id)          
        date_month = self.request.GET.get('date_month')
        if date_month:
            date_month = date_month.split("-", 1)
            orcamento = orcamento.filter(data__month=date_month[1],data__year=date_month[0])
        return orcamento


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


class OrcamentoCreateView( PassRequestToFormView, CreateView ):
    model = Orcamento
    form_class = OrcamentoForm
    template_name='Orcamento/adicionarOrcamento.html'
    success_url = reverse_lazy('orcamento')

    def form_valid(self, form):
        form.instance.categoria__id_user = self.request.user.id
        self.object = form.save(commit=False)
        self.object.id_user = self.request.user
        self.object.save()
        return super().form_valid(form)


class OrcamentoUpdate(PassRequestToFormView, UpdateView):
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