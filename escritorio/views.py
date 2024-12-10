from django.shortcuts import get_object_or_404, render
from escritorio.models import Escritorio

def escritorio_detalhes(request):
    escritorio = request.user.escritorio
    
    return render(request, 'escritorio_detalhes.html', {'escritorio': escritorio})