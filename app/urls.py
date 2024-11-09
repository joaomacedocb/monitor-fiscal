from django.contrib import admin
from django.urls import path
from clientes.views import clientes_view, novo_cliente_view, atualizar_clientes_view
from escritorio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('escritorio/<int:id>/', views.escritorio_detalhes, name='escritorio_detalhes'),
    path('clientes/', clientes_view, name='clientes'),
    path('novo_cliente/', novo_cliente_view, name='novo_cliente'),
    path('atualizar-clientes/', atualizar_clientes_view, name='atualizar_clientes'),
]