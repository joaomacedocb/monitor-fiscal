# Generated by Django 5.1.2 on 2024-12-05 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0015_alter_consultahistorico_tipo_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultahistorico',
            name='escritorio',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Escritorio'),
        ),
    ]
