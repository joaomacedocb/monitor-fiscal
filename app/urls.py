from django.contrib import admin
from django.urls import path
from clientes.views import ClienteDetailView, ClienteUpdateView, ClienteDeleteView, buscar_cnpj, clientes_view, novo_cliente_view, atualizar_clientes_view
from configuracoes.views import minha_configuracao
from escritorio.views import escritorio_detalhes
from contas.views import register_view, login_view, logout_view
from inicio.views import inicio_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('escritorio/', escritorio_detalhes, name='escritorio_detalhes'),
    path('configuracoes/', minha_configuracao, name='configuracoes'),
    path('clientes/', clientes_view, name='clientes'),
    path('novo_cliente/', novo_cliente_view, name='novo_cliente'),
    path('atualizar-clientes/', atualizar_clientes_view, name='atualizar_clientes'),
    path('api/buscar-cnpj/', buscar_cnpj, name='buscar_cnpj'),
    path('cliente/<int:pk>/', ClienteDetailView.as_view(), name = 'cliente_detalhe'),
    path('cliente/<int:pk>/update/', ClienteUpdateView.as_view(), name = 'cliente_update'),
    path('cliente/<int:pk>/delete/', ClienteDeleteView.as_view(), name = 'cliente_delete'),
    path('registro/', register_view, name='register_view'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', inicio_view, name='inicio'),
]