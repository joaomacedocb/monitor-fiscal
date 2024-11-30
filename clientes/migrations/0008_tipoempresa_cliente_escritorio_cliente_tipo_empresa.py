# Generated by Django 5.1.2 on 2024-11-27 01:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_alter_cliente_data_exclusao_and_more'),
        ('escritorio', '0003_escritorio_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoEmpresa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Tipo Empresa',
                'verbose_name_plural': 'Tipos Empresa',
            },
        ),
        migrations.AddField(
            model_name='cliente',
            name='escritorio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='escritorio', to='escritorio.escritorio'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='tipo_empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tipo_empresa', to='clientes.tipoempresa'),
        ),
    ]