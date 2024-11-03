from django.contrib import admin
from escritorio.models import Escritorio

class EscritorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cnpj', 'cep', 'endereco', 'numero', 'cidade', 'uf', 'responsavel_tecnico', 'email', 'telefone')
    search_fields = ('id','cnpj','nome','email')

admin.site.register(Escritorio, EscritorioAdmin)