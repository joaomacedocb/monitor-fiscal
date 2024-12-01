from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
import requests
from clientes.models import Cliente
from clientes.forms import ClienteForm
from django.views.generic import DetailView, UpdateView, DeleteView
from clientes.consulta_e_atualiza_clientes import consulta_e_atualiza_clientes
from django.db.models import Q

@login_required
def clientes_view(request):
    clientes = Cliente.objects.all().order_by('nome_fantasia')
    
    search = request.GET.get('search', '')
    status = request.GET.get('status', '')
    
    if search:
        clientes = clientes.filter(Q(nome_fantasia__icontains = search) | Q(cnpj__icontains = search))
    
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
            novo_cliente_form.save()
            return redirect('clientes')
    else:
        novo_cliente_form = ClienteForm()
    return render(request, 'novo_cliente.html', { 'novo_cliente_form': novo_cliente_form })

@login_required
def atualizar_clientes_view(request):
    consulta_e_atualiza_clientes()
    messages.success(request, "Os dados dos clientes foram atualizados com sucesso.")
    return redirect('clientes')

from django.http import JsonResponse

@login_required
def buscar_cnpj(request):
    
    cnpj = request.GET.get('cnpj')
    
    if not cnpj:
        return JsonResponse({'error': 'CNPJ não fornecido.'}, status=400)
    
    url = f'https://publica.cnpj.ws/cnpj/{cnpj}'
    
    try:
        resp = requests.get(url)
        
        if resp.status_code == 200:
            
            data = resp.json()
            razao_social = data.get("razao_social")
            estabelecimento = data.get('estabelecimento', {})
            nome_fantasia = estabelecimento.get("nome_fantasia")
            email = estabelecimento.get("email")
            ddd = estabelecimento.get("ddd1")
            telefone = estabelecimento.get("telefone1")
            
            socios = data.get("socios", [])
            if socios and isinstance(socios, list):
                responsavel = socios[0].get("nome", "Não informado")
            else:
                responsavel = "Não informado"
        
    except:
        ...

    dados = {
        "razao_social": razao_social,
        "estabelecimento": {
            "nome_fantasia": nome_fantasia,
            "email": email,
            "telefone1": ddd + telefone,
        },
        "responsavel": responsavel
    }

    return JsonResponse(dados)

@method_decorator(login_required, name='dispatch')
class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente_detalhe.html'

@method_decorator(login_required, name='dispatch')
class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente_update.html'
    success_url = reverse_lazy('clientes')

@method_decorator(login_required, name='dispatch')
class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente_delete.html'
    success_url = reverse_lazy('clientes')