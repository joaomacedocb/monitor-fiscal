from django.contrib import admin
from .models import Configuracoes

class ConfiguracoesAdmin(admin.ModelAdmin):
    list_display = ('cor_principal','empresa_config', 'email_notificacao', 'envia_notificacao')
    search_fields = ('empresa_config',)

admin.site.register(Configuracoes, ConfiguracoesAdmin)