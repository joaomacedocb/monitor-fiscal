from django.contrib import admin
from django.urls import path
from escritorio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('escritorio/<int:id>/', views.escritorio_detalhes, name='escritorio_detalhes'),
]