from meuOrcamento.models import *

class Categoria(models.Model):
    nome = models.CharField(max_length = 150)
    descricao = models.TextField()
    
    
    def __str__(self):
        return '{}'.format(self.nome)