# Generated by Django 5.1.2 on 2024-11-30 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escritorio', '0003_escritorio_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='escritorio',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]
