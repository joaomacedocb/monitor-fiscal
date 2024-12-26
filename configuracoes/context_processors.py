from configuracoes.models import Configuracoes
from django.conf import settings

def cor_principal(request):
    if request.user.is_authenticated:
        escritorio = request.user.escritorio
        try:
            configuracoes = Configuracoes.objects.get(empresa_config=escritorio)
            cor_principal = configuracoes.cor_principal or "#001f3f"
        except Configuracoes.DoesNotExist:
            cor_principal = "#001f3f"
    else:
        cor_principal = "#001f3f"
    
    return {
        'cor_principal': cor_principal
    }
