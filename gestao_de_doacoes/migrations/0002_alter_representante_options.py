# Generated by Django 4.0.1 on 2022-01-12 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_de_doacoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='representante',
            options={'ordering': ['representante__username'], 'verbose_name': 'Representante de entidade', 'verbose_name_plural': 'Representantes de entidades'},
        ),
    ]