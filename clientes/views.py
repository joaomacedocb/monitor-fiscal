from django.shortcuts import render
from clientes.models import Cliente

def clientes_view(request):
    clientes = Cliente.objects.all().order_by('nome_fantasia')
    search = request.GET.get('search')
    
    if search:
        clientes = clientes.filter(nome_fantasia__icontains = search)
        
    return render(request, 'clientes.html', {'clientes': clientes})
