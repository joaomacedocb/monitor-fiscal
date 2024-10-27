from django.db import models
from django.core.validators import RegexValidator

class Escritorio(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=14, blank=True, null=True)
    cep = models.CharField(
        max_length=9, 
        validators=[
            RegexValidator(regex=r'^\d{5}-\d{3}$', message="CEP deve estar no formato 99999-999.")
        ],
    )
    endereco = models.CharField(max_length=100, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    responsavel_tecnico = models.CharField(max_length=50)
    telefone = models.CharField(
        max_length=15, blank=True, null=True,
        validators=[
            RegexValidator(
                regex=r'^\(?\d{2}\)? ?9?\d{4}-\d{4}$',
                message="O número de telefone deve estar no formato (99) 99999-9999 ou (99) 9999-9999."
            )
        ]
    )