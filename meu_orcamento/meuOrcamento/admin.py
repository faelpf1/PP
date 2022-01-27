from django.contrib import admin
from .models import *


class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo_orcamento','valorEmReais', 'dataOrcamento',)
    empty_value_display = 'Vazio'
    search_fields = ('nome', 'tipo_orcamento', 'data',)
    def valorEmReais(self, obj):
        return 'R$'+str(obj.valor)

    def dataOrcamento(self, obj):
        if obj.data:
            return obj.data.strftime("%d/%m/%Y")
    dataOrcamento.empty_value_display = '__/__/____'


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    empty_value_display = 'Vazio'
    search_fields = ('nome',)


admin.site.register(Orcamento, OrcamentoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
