from django.db import models

class Orcamento(models.Model):
    nome = models.CharField( max_length = 200 )
    valor = models.FloatField( )
    data = models.DateField( )
    id_categoria = models.ForeignKey('Categoria', on_delete = models.SET_NULL, null = True)   
    tipo = models.CharField( 
                    max_length = 8, 
                    choices = ( ( 'Receita','Receita' ), ( 'Despesa','Despesa' ) ),
                    default = 'Despesa',
                    )
    def __str__(self):
        return self.nome

  
class Categoria(models.Model):
    nome = models.CharField( max_length = 200, unique = True)
    descricao = models.TextField()
    def __str__(self):
        return self.nome