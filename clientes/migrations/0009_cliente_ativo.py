# Generated by Django 5.1.2 on 2024-11-30 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0008_tipoempresa_cliente_escritorio_cliente_tipo_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]