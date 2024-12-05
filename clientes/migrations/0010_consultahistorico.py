# Generated by Django 5.1.2 on 2024-12-05 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0009_cliente_ativo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultaHistorico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(db_index=True, max_length=14, verbose_name='CNPJ')),
                ('regime_fiscal', models.CharField(blank=True, max_length=100, null=True, verbose_name='Regime Fiscal')),
                ('porte_empresa', models.CharField(blank=True, max_length=50, null=True, verbose_name='Porte da Empresa')),
                ('data_consulta', models.DateTimeField(auto_now_add=True, verbose_name='Data da Consulta')),
                ('status', models.CharField(choices=[('SUCCESS', 'Sucesso'), ('FAILED', 'Falha')], default='SUCCESS', max_length=20, verbose_name='Status da Consulta')),
                ('detalhes', models.TextField(blank=True, null=True, verbose_name='Detalhes da Consulta')),
            ],
            options={
                'verbose_name': 'Histórico de Consulta',
                'verbose_name_plural': 'Históricos de Consulta',
                'ordering': ['-data_consulta'],
            },
        ),
    ]
