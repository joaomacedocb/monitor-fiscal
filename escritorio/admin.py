from django.contrib import admin
from escritorio.models import Escritorio

class EscritorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cnpj', 'cep', 'endereco', 'numero', 'cidade', 'uf', 'responsavel_tecnico', 'telefone')
    search_fields = ('id','cnpj','nome')

admin.site.register(Escritorio, EscritorioAdmin)