from functools import wraps
from django.http import HttpResponse, HttpResponseForbidden
from django.core.exceptions import PermissionDenied


from clientes.models import Cliente

def filtrar_clientes_por_escritorio(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden("Usuário não autenticado.")

        escritorio = getattr(request.user, 'escritorio', None)
        if not escritorio:
            return HttpResponse("""
        <html>
            <head>
                <style>
                    body {
                        background-color: #721c24;
                        color: white;
                        font-family: Arial, sans-serif;
                        text-align: center;
                        padding-top: 100px;
                    }
                    h1 {
                        font-size: 24px;
                    }
                    .btn-voltar {
                        background-color: lightgrey;
                        color: #721c24;
                        border: none;
                        padding: 10px 20px;
                        font-size: 16px;
                        cursor: pointer;
                        margin-top: 20px;
                        text-decoration: none;
                        border-radius: 5px;
                    }
                    .btn-voltar:hover {
                        background-color: #f5c6cb;
                    }
                </style>
            </head>
            <body>
                <h1>O usuário deve ser associado à um escritório. Verifique com o Administrador do sistema.</h1>
                <a href="javascript:window.history.back();" class="btn-voltar">Voltar</a>
            </body>
        </html>
    """)

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