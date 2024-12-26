from django.db import models

from escritorio.models import Escritorio

class Configuracoes(models.Model):
    cor_principal = models.TextField(null=True, blank=True)
    empresa_config = models.ForeignKey(Escritorio, on_delete=models.CASCADE)