# Generated by Django 5.1.2 on 2024-12-05 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0010_consultahistorico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultahistorico',
            name='detalhes',
        ),
    ]
