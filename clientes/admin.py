from django.contrib import admin
from clientes.models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'cnpj', 'nome_fantasia', 'razao_social', 'email', 'telefone')
    search_fields = ('id','cnpj', 'nome_fantasia', 'razao_social','email')

admin.site.register(Cliente, ClienteAdmin)
