# Generated by Django 3.2.5 on 2022-01-15 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receita',
            name='dataPagamentoEsperado',
        ),
    ]
