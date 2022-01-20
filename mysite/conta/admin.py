from django.contrib import admin
from .models import Orcamento
from .models import Categoria


@admin.register(Orcamento)
class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ( "nome", "valor", "tipo", "data", "id_categoria" )

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ( "nome", "descricao" )