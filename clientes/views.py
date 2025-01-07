from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
import requests
from clientes.models import Cliente, RegimeFiscal
from clientes.forms import ClienteForm
from django.views.generic import DetailView, UpdateView, DeleteView
from clientes.consulta_e_atualiza_clientes import consulta_e_atualiza_clientes
from django.db.models import Q
import logging
from django.http import JsonResponse

logger = logging.getLogger(__name__)

from clientes.utils import EscritorioRestritoMixin, filtrar_clientes_por_escritorio

@filtrar_clientes_por_escritorio
@login_required
def clientes_view(request):

    clientes = request.clientes.order_by('nome_fantasia')
    
    search = request.GET.get('search', '')
    status = request.GET.get('status', '')
    
    if search:
        clientes = clientes.filter(Q(nome_fantasia__icontains=search) | Q(cnpj__icontains=search))
    
    if status == 'ativo':
        clientes = clientes.filter(ativo=True)
    elif status == 'inativo':
        clientes = clientes.filter(ativo=False)
        
    return render(request, 'clientes.html', {'clientes': clientes})

@login_required
def novo_cliente_view(request):
    if request.method == 'POST':
        novo_cliente_form = ClienteForm(request.POST)
        if novo_cliente_form.is_valid():
            cliente = novo_cliente_form.save(commit = False)
            cliente.escritorio = request.user.escritorio
            cliente.save()
            return redirect('clientes')
    else:
        novo_cliente_form = ClienteForm()
    return render(request, 'novo_cliente.html', { 'novo_cliente_form': novo_cliente_form })

@login_required
def atualizar_clientes_view(request):
    try:
        consulta_e_atualiza_clientes(request.user)
        messages.success(request, "Os dados dos clientes foram atualizados com sucesso.")
    except Exception as e:
        messages.error(request, f"Ocorreu um erro ao atualizar os dados dos clientes: {str(e)}")
    return redirect('clientes')

@login_required
def buscar_cnpj(request):
    
    cnpj = request.GET.get('cnpj')
    
    if not cnpj:
        return JsonResponse({'error': 'CNPJ não fornecido.'}, status=400)
    
    if not cnpj.isdigit() or len(cnpj) != 14:
        return JsonResponse({'error': 'CNPJ fornecido não está no formato correto.'}, status=400)
    
    url = f'https://publica.cnpj.ws/cnpj/{cnpj}'
    
    try:
        logger.info(f'Buscando dados para o CNPJ: {cnpj}')
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        
        data = resp.json()
        logger.info(f'Dados retornados pela API: {data}')
        
        simples = data.get('simples', {})
        
        regime_simples = simples.get('simples', 'Não')
        regime_mei = simples.get('mei', 'Não')
        
        porte = data.get('porte', {})
        
        consulta_porte = porte.get('id', None)
        
        razao_social = data.get("razao_social", "Não informado")
        estabelecimento = data.get('estabelecimento', {})
        nome_fantasia = estabelecimento.get("nome_fantasia") or data.get("razao_social") or "Não informado"
        email = estabelecimento.get("email") or "nao@informado.com"
        ddd = estabelecimento.get("ddd1") or "00"
        telefone = estabelecimento.get("telefone1") or "000000000"

        socios = data.get("socios", [])
        
        if socios and isinstance(socios, list):
            responsavel = socios[0].get("nome", "Não informado")
        else:
            responsavel = "Não informado"
            
        if regime_simples == "Sim" and regime_mei == "Sim":
            regime_fiscal_id = 2  # SIMEI
        elif regime_simples == "Sim" and regime_mei == "Não":
            regime_fiscal_id = 1  # SIMPLES NACIONAL
        else:
            regime_fiscal_id = None
            
        if consulta_porte == "01":
            tipo_empresa_id = 1 # MICRO EMPRESA
        elif consulta_porte == "03":
            tipo_empresa_id = 2 # EMPRESA PEQUENO PORTE
        else:
            tipo_empresa_id = None
            
            
            
        dados = {
        "razao_social": razao_social,
        "estabelecimento": {
            "nome_fantasia": nome_fantasia,
            "email": email,
            "telefone1": ddd + telefone,
        },
        "responsavel": responsavel,
        "tipo_empresa": tipo_empresa_id,
        "regime_fiscal": regime_fiscal_id,
        }
        
        logger.info(f'Dados processados: {dados}')
        return JsonResponse(dados)    
        
    except requests.exceptions.RequestException as e:
        logger.error(f'Erro ao consultar a API: {e}')
        return JsonResponse({'error': 'Erro ao consultar o CNPJ. Tente novamente mais tarde.'}, status=500)

    except KeyError as e:
        logger.error(f'Erro ao processar a resposta: campo {str(e)} não encontrado.')
        return JsonResponse({'error': f'Erro ao processar a resposta: campo {str(e)} não encontrado.'}, status=500)

    except Exception as e:
        logger.error(f'Erro inesperado: {e}')
        return JsonResponse({'error': 'Erro inesperado. Contate o suporte.'}, status=500)

@method_decorator(login_required, name='dispatch')
class ClienteDetailView(EscritorioRestritoMixin, DetailView):
    model = Cliente
    template_name = 'cliente_detalhe.html'

@method_decorator(login_required, name='dispatch')
class ClienteUpdateView(EscritorioRestritoMixin, UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_update.html'
    success_url = reverse_lazy('clientes')

@method_decorator(login_required, name='dispatch')
class ClienteDeleteView(EscritorioRestritoMixin, DeleteView):
    model = Cliente
    template_name = 'cliente_delete.html'
    success_url = reverse_lazy('clientes')