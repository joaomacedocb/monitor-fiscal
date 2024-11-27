from django.db import models
from django.core.validators import RegexValidator
from escritorio.models import Escritorio

class RegimeFiscal(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Regime Fiscal"
        verbose_name_plural = "Regimes Fiscais"
        
class TipoEmpresa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Tipo Empresa"
        verbose_name_plural = "Tipos Empresa"

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome_fantasia = models.CharField(max_length=200)
    razao_social = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=14, blank=True, null=True)
    responsavel_tecnico = models.CharField(max_length=50)
    email = models.CharField(max_length=200, blank=True, null=True)
    tipo_empresa = models.ForeignKey(TipoEmpresa, on_delete=models.PROTECT, related_name='tipo_empresa', blank= True, null= True)
    regime_fiscal = models.ForeignKey(RegimeFiscal, on_delete=models.PROTECT, related_name= 'regime_fiscal')
    data_inclusao = models.DateField(blank= True, null= True)
    data_exclusao = models.DateField(blank= True, null= True)
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
    escritorio = models.ForeignKey(Escritorio, on_delete=models.PROTECT, related_name='escritorio', blank= True, null= True)
    
    def __str__(self):
        return self.nome_fantasia