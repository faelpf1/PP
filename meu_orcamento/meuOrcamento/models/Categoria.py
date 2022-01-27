from meuOrcamento.models import *

class Categoria(models.Model):
    nome = models.CharField(max_length = 150)
    descricao = models.TextField()
    id_user = models.ForeignKey(User, null = True, related_name='idUserC', on_delete= models.SET_NULL)
    
    
    def __str__(self):
        return '{}'.format(self.nome)