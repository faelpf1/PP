from django.forms import ModelForm
from django import forms
from meuOrcamento.models import Orcamento

class OrcamentoForm(ModelForm):
    def __init__( self, *args, **kwargs ):
        super( OrcamentoForm, self ).__init__( *args, **kwargs )
    #self.fields['categoria'].queryset = Categoria.objects.filter(user_id = self.request.user.id)
    #categoria = forms.ModelChoiceField(queryset=Categoria.objects.filter(id_user=self.request.user.id), widget=forms.Select(attrs={'class': "form-control"}))
    class Meta:
        model = Orcamento
        fields = ['nome', 'data', 'tipo_orcamento', 'categoria', 'valor']
        widgets = {
            'nome': forms.TextInput( attrs = {'class': "form-control"} ),
            'data': forms.DateInput( attrs = {'class': "form-control", "type": "date"} ),
            'tipo_orcamento': forms.Select( attrs = {'class': "form-control"} ),
            'categoria': forms.Select( attrs = {'class': "form-control"} ),
            'valor': forms.TextInput( attrs = {'class': "form-control"} ),
        }


    
