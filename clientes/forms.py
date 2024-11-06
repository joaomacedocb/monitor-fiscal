from django import forms
from django.core.validators import RegexValidator

from django import forms
from django.core.validators import RegexValidator

from clientes.models import RegimeFiscal

class ClienteForm(forms.Form):
    nome_fantasia = forms.CharField(
        max_length=200,
        label="Nome Fantasia"
    )
    razao_social = forms.CharField(
        max_length=200,
        label="Razão Social"
    )
    cnpj = forms.CharField(
        max_length=14,
        required=False,
        label="CNPJ"
    )
    responsavel_tecnico = forms.CharField(
        max_length=50,
        label="Responsável"
    )
    email = forms.EmailField(
        required=False,
        label="E-mail"
    )
    regime_fiscal = forms.ModelChoiceField(RegimeFiscal.objects.all(), label="Regime Fiscal")

    telefone = forms.CharField(
        max_length=15,
        required=False,
        label="Telefone",
        validators=[
            RegexValidator(
                regex=r'^\d{10,11}$',
                message="O número de telefone deve conter apenas dígitos e ter 10 ou 11 dígitos."
            )
        ]
    )
