from meuOrcamento.models import *

class Orcamento(models.Model):
    categoria = models.ForeignKey(Categoria, null = True, related_name='categoria', on_delete = models.SET_NULL)
    nome = models.CharField(max_length = 255)
    tipo_orcamento = models.IntegerField(choices = TIPO_ORCAMENTO, default = '2')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(Perfil, on_delete=models.CASCADE)  
    
    def __str__(self):
        return '{}'.format(self.nome)