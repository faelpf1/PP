# Generated by Django 4.0.1 on 2022-01-25 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meuOrcamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='privilegio',
            field=models.IntegerField(choices=[(1, 'Administrador'), (2, 'Usuário')], default=2),
        ),
    ]
