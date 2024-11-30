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
    complemento = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    responsavel_tecnico = models.CharField(max_length=50)
    email = models.CharField(max_length=200, blank=True, null=True)
    telefone = models.CharField(
        max_length=15, blank=True, null=True,
        validators=[
            RegexValidator(
                regex=r'^\d{10,11}$',
                message="O número de telefone deve conter apenas dígitos e ter 10 ou 11 dígitos."
            )
        ]
    )
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome