from django import forms

from .models import Categoria, Orcamento

class adicionarCategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nome', 'descricao')


class adicionarOrcamentoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        fields = ('nome','valor', 'data', 'id_categoria', 'tipo')