from django import forms
from django.core.validators import RegexValidator

from django import forms
from django.core.validators import RegexValidator

from clientes.models import RegimeFiscal, Cliente

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

    def save(self):
        cliente = Cliente(
            nome_fantasia = self.cleaned_data['nome_fantasia'],
            razao_social = self.cleaned_data['razao_social'],
            cnpj = self.cleaned_data['cnpj'],
            responsavel_tecnico = self.cleaned_data['responsavel_tecnico'],
            email = self.cleaned_data['email'],
            regime_fiscal = self.cleaned_data['regime_fiscal'],
            telefone = self.cleaned_data['telefone'],
            status = 'Em análise',
        )
        cliente.save()
        return cliente
