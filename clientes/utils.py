from functools import wraps
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied


from clientes.models import Cliente

def filtrar_clientes_por_escritorio(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden("Usuário não autenticado.")

        escritorio = getattr(request.user, 'escritorio', None)
        if not escritorio:
            return HttpResponseForbidden("Usuário não pertence a nenhum escritório.")

        request.clientes = Cliente.objects.filter(escritorio=escritorio)
        return view_func(request, *args, **kwargs)

    return _wrapped_view

class EscritorioRestritoMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        escritorio = self.request.user.escritorio
        return qs.filter(escritorio=escritorio)

    def dispatch(self, request, *args, **kwargs):
        if hasattr(self, 'get_object'):
            obj = self.get_object()
            if obj.escritorio != request.user.escritorio:
                raise PermissionDenied("Você não tem permissão para acessar este recurso.")
        return super().dispatch(request, *args, **kwargs)