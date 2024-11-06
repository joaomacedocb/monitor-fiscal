from django.shortcuts import render
from clientes.models import Cliente
from clientes.forms import ClienteForm

def clientes_view(request):
    clientes = Cliente.objects.all().order_by('nome_fantasia')
    search = request.GET.get('search')
    
    if search:
        clientes = clientes.filter(nome_fantasia__icontains = search)
        
    return render(request, 'clientes.html', {'clientes': clientes})


def novo_cliente_view(request):
    
    novo_cliente_form = ClienteForm()
    return render(request, 'novo_cliente.html', { 'novo_cliente_form': novo_cliente_form })