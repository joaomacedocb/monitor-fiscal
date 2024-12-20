# Generated by Django 5.1.2 on 2024-11-02 22:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome_fantasia', models.CharField(max_length=200)),
                ('razao_social', models.CharField(max_length=200)),
                ('cnpj', models.CharField(blank=True, max_length=14, null=True)),
                ('responsavel_tecnico', models.CharField(max_length=50)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('telefone', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message='O número de telefone deve conter apenas dígitos e ter 10 ou 11 dígitos.', regex='^\\d{10,11}$')])),
            ],
        ),
        migrations.DeleteModel(
            name='Clientes',
        ),
    ]
