from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from clientes.models import Cliente
from clientes.forms import ClienteForm
from django.views.generic import DetailView, UpdateView, DeleteView
from clientes.consulta_e_atualiza_clientes import consulta_e_atualiza_clientes

@login_required
def clientes_view(request):
    clientes = Cliente.objects.all().order_by('nome_fantasia')
    search = request.GET.get('search')
    
    if search:
        clientes = clientes.filter(nome_fantasia__icontains = search)
        
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