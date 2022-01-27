from django.forms import ModelForm
from django import forms
from meuOrcamento.models import Orcamento

class OrcamentoForm(ModelForm):
    class Meta:
        model = Orcamento
        fields = ['nome', 'data', 'tipo_orcamento', 'categoria', 'valor']
        widgets = {
            'nome': forms.TextInput(attrs={'class': "form-control"}),
            'data': forms.DateInput(attrs={'class': "form-control", "type": "date"}),
            'tipo_orcamento': forms.Select(attrs={'class': "form-control"}),
            'categoria': forms.Select(attrs={'class': "form-control"}),
            'valor': forms.TextInput(attrs={'class': "form-control"}),
        }
