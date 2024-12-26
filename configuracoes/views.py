from django.shortcuts import render, get_object_or_404
from .models import Configuracoes, Escritorio

def meu_template(request, empresa_id):

    empresa = get_object_or_404(Escritorio, id=empresa_id)

    try:
        configuracoes = Configuracoes.objects.get(empresa_config=empresa)
        cor_principal = configuracoes.cor_principal or "#001f3f"
    except Configuracoes.DoesNotExist:

        cor_principal = "#001f3f"

    return render(request, 'base.html', {'cor_principal': cor_principal})

