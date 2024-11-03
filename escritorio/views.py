from django.shortcuts import get_object_or_404, render
from escritorio.models import Escritorio

def escritorio_detalhes(request, id):
    escritorio = get_object_or_404(Escritorio, id=id)
    return render(request, 'escritorio_detalhes.html', {'escritorio': escritorio})