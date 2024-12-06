from django.shortcuts import render
from clientes.models import ConsultaHistorico
from django.core.paginator import Paginator

def inicio_view(request):
    total_consultas = ConsultaHistorico.objects.count()
    total_exclusoes = ConsultaHistorico.objects.filter(data_exclusao__isnull=False).count()
    consultas_list = ConsultaHistorico.objects.all().order_by('-data_consulta')
    
    paginator = Paginator(consultas_list, 10)
    page_number = request.GET.get('page')
    consultas = paginator.get_page(page_number) 
    
    context = {
        'total_consultas': total_consultas,
        'total_exclusoes': total_exclusoes,
        'consultas': consultas,
    }
    return render(request, 'inicio.html', context)

