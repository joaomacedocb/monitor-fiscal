# Generated by Django 5.1.2 on 2024-11-06 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_regimefiscal_alter_cliente_regime_fiscal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='regimefiscal',
            options={'verbose_name': 'Regime Fiscal', 'verbose_name_plural': 'Regimes Fiscais'},
        ),
    ]