from django.contrib import admin
from clientes.models import Cliente, RegimeFiscal, TipoEmpresa

class RegimeFiscalAdm(admin.ModelAdmin):
    list_display = ('id','nome')
    search_fields = ('id','nome')
    
class TipoEmpresaAdmin(admin.ModelAdmin):
    list_display = ('id','nome')
    search_fields = ('id','nome')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'cnpj', 'nome_fantasia', 'razao_social', 'email', 'telefone', 'tipo_empresa', 'regime_fiscal', 'ultima_atualizacao', 'status')
    search_fields = ('id','cnpj', 'nome_fantasia', 'razao_social','email')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(RegimeFiscal, RegimeFiscalAdm)
admin.site.register(TipoEmpresa, TipoEmpresaAdmin)
