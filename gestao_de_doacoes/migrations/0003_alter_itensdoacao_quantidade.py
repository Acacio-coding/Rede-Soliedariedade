# Generated by Django 4.0.1 on 2022-01-18 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_de_doacoes', '0002_alter_itensdoacao_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itensdoacao',
            name='quantidade',
            field=models.PositiveIntegerField(help_text='Digite a quantidade do item selecionado'),
        ),
    ]
