from django.db import models
from django.core.validators import RegexValidator

class RegimeFiscal(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Regime Fiscal"
        verbose_name_plural = "Regimes Fiscais"

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome_fantasia = models.CharField(max_length=200)
    razao_social = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=14, blank=True, null=True)
    responsavel_tecnico = models.CharField(max_length=50)
    email = models.CharField(max_length=200, blank=True, null=True)
    regime_fiscal = models.ForeignKey(RegimeFiscal, on_delete=models.PROTECT, related_name= 'regime_fiscal')
    ultima_atualizacao = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, blank= True, null= True)
    telefone = models.CharField(
        max_length=15, blank=True, null=True,
        validators=[
            RegexValidator(
                regex=r'^\d{10,11}$',
                message="O número de telefone deve conter apenas dígitos e ter 10 ou 11 dígitos."
            )
        ]
    )
    
    def __str__(self):
        return self.nome_fantasia