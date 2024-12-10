from django.shortcuts import render
from clientes.models import ConsultaHistorico
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def inicio_view(request):
    escritorio = request.user.escritorio
    
    consultas_list = ConsultaHistorico.objects.filter(escritorio=escritorio).order_by('-data_consulta')
    
    total_consultas = consultas_list.count()
    total_exclusoes = consultas_list.filter(data_exclusao__isnull=False).count()
    
    paginator = Paginator(consultas_list, 10)
    page_number = request.GET.get('page')
    consultas = paginator.get_page(page_number)
    
    context = {
        'total_consultas': total_consultas,
        'total_exclusoes': total_exclusoes,
        'consultas': consultas,
    }
    
    return render(request, 'inicio.html', context)