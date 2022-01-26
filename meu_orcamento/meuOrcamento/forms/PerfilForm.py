from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from meuOrcamento.models.Perfil import Perfil

class PerfilForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PerfilForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.privilegio != 1:
            del self.fields['privilegio']        

    class Meta:
        model = Perfil
        fields = ('usuario', 'privilegio',)
        widgets = {
            'usuario': forms.HiddenInput(),
            'privilegio': forms.Select(attrs={'class': "form-control"}),
        }

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': "form-control"}),
            'email': forms.EmailInput(attrs={'class': "form-control"}),
        }