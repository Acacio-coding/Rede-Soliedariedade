# Generated by Django 4.0.1 on 2022-01-18 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_de_doacoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itensdoacao',
            options={'ordering': ['doacao'], 'verbose_name': 'Item de doação', 'verbose_name_plural': 'Itens de doações'},
        ),
        migrations.AlterField(
            model_name='itensdoacao',
            name='quantidade',
            field=models.IntegerField(help_text='Digite a quantidade do item selecionado'),
        ),
    ]