# Generated by Django 4.0.1 on 2022-01-12 23:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestao_de_doacoes', '0004_alter_representante_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doacao',
            name='data_cadastro',
            field=models.DateField(auto_now_add=True, verbose_name='data de cadastro'),
        ),
        migrations.AlterField(
            model_name='doacao',
            name='usuario',
            field=models.ForeignKey(help_text='Selecione o usuário representante', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='usuário'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='cnpj',
            field=models.CharField(help_text='Digite o cnpj da entidade', max_length=14),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='data_cadastro',
            field=models.DateField(auto_now_add=True, verbose_name='data de cadastro'),
        ),
        migrations.AlterField(
            model_name='entidade',
            name='representante',
            field=models.ForeignKey(help_text='Selecione o representante da entidade', on_delete=django.db.models.deletion.CASCADE, to='gestao_de_doacoes.representante'),
        ),
        migrations.AlterField(
            model_name='familia',
            name='data_cadastro',
            field=models.DateField(auto_now_add=True, verbose_name='data de cadastro'),
        ),
        migrations.AlterField(
            model_name='integrantefamiliar',
            name='cpf',
            field=models.CharField(help_text='Digite o cpf do integrante da família', max_length=11),
        ),
        migrations.AlterField(
            model_name='integrantefamiliar',
            name='data_cadastro',
            field=models.DateField(auto_now_add=True, verbose_name='data de cadastro'),
        ),
        migrations.AlterField(
            model_name='integrantefamiliar',
            name='telefone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Digite o telefone do integrante da família (00)0 0000-0000 (opcional)', max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='itensdoacao',
            name='doacao',
            field=models.ForeignKey(help_text='Selecione a doação', on_delete=django.db.models.deletion.CASCADE, to='gestao_de_doacoes.doacao'),
        ),
        migrations.AlterField(
            model_name='itensdoacao',
            name='item',
            field=models.ForeignKey(help_text='Selecione o item', on_delete=django.db.models.deletion.CASCADE, to='gestao_de_doacoes.item'),
        ),
        migrations.AlterField(
            model_name='itensdoacao',
            name='quantidade',
            field=models.PositiveIntegerField(help_text='Digite a quantidade do item selecionado'),
        ),
        migrations.AlterField(
            model_name='representante',
            name='cpf',
            field=models.CharField(help_text='Digite o cpf do representante da entidade', max_length=11),
        ),
        migrations.AlterField(
            model_name='representante',
            name='data_cadastro',
            field=models.DateField(auto_now_add=True, verbose_name='data de cadastro'),
        ),
        migrations.AlterField(
            model_name='representante',
            name='nome',
            field=models.CharField(help_text='Digite o nome do representante da entidade', max_length=200),
        ),
        migrations.AlterField(
            model_name='representante',
            name='representante',
            field=models.ForeignKey(help_text='Selecione o usuário representante', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]