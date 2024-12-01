from django import forms
from django.core.validators import RegexValidator

from django import forms
from django.core.validators import RegexValidator

from clientes.models import Cliente

class ClienteForm(forms.ModelForm):
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

    class Meta:
        model = Cliente
        fields = [
            'cnpj', 
            'nome_fantasia', 
            'razao_social', 
            'responsavel_tecnico', 
            'email',
            'tipo_empresa',
            'regime_fiscal', 
            'telefone',
            'ativo',
        ]
        labels = {
            'cnpj': "CNPJ",
            'nome_fantasia': "Nome Fantasia",
            'razao_social': "Razão Social",
            'responsavel_tecnico': "Responsável",
            'email': "E-mail",
            'tipo_empresa': "Tipo da Empresa",
            'regime_fiscal': "Regime Fiscal",
            'telefone': "Telefone",
            'ativo': "Ativo"
        }

    def save(self, commit=True):
        cliente = super().save(commit=False)
        
        cliente.nome_fantasia = self.cleaned_data['nome_fantasia'].upper()
        cliente.razao_social = self.cleaned_data['razao_social'].upper()
        cliente.responsavel_tecnico = self.cleaned_data['responsavel_tecnico'].upper()
        
        if cliente.status == None:
            cliente.status = 'Em análise'
        if commit:
            cliente.save()
        return cliente
    
    def clean_cnpj(self):
        cnpj = self.cleaned_data['cnpj']
        cliente_id = self.instance.pk
        
        if Cliente.objects.filter(cnpj=cnpj).exclude(pk=cliente_id).exists():
            raise forms.ValidationError('O CNPJ informado já existe na base de dados.')
        
        return cnpj