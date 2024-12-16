from django.db import models

class Configuracoes(models.Model):
    cores = models.TextField(null=True, blank=True)