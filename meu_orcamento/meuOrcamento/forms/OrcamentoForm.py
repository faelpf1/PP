from django.forms import ModelForm
from django import forms
from meuOrcamento.models import Orcamento, Categoria

class OrcamentoForm(ModelForm):
    def __init__( self, *args, **kwargs ):
        self.request = kwargs.pop("request")
        super( OrcamentoForm, self ).__init__( *args, **kwargs )
        self.fields['categoria'].queryset = Categoria.objects.filter(id_user=self.request.user.id)
    class Meta:
        model = Orcamento
        fields = ['nome', 'data', 'tipo_orcamento', 'categoria', 'valor']
        widgets = {
            'nome': forms.TextInput( attrs = {'class': "form-control"} ),
            'data': forms.DateInput( attrs = {'class': "form-control", "type": "date", }, format='%Y-%m-%d'),
            'tipo_orcamento': forms.Select( attrs = {'class': "form-control"} ),
            'categoria': forms.Select(attrs = {'class': "form-control"} ),
            'valor': forms.TextInput( attrs = {'class': "form-control"} ),
        }

    categoria = forms.ModelChoiceField(queryset=None, widget=forms.Select(attrs={'class': "form-control"}))


    
