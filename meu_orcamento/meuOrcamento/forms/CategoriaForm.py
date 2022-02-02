from django.forms import ModelForm
from django import forms
from meuOrcamento.models import Categoria

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'descricao', ]
        widgets = {
            'nome': forms.TextInput(attrs={'class': "form-control"}),
            'descricao': forms.Textarea(attrs={'class': "form-control"}),
        }
