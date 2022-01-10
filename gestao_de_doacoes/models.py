from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import datetime

# Create your models here.
class Familia(models.Model):
    chefe_da_familia = models.CharField(max_length=200, help_text='Digite o nome do chefe da família')
    cpf = models.CharField(max_length=11, help_text='Digite o cpf do chefe da família')
    endereco = models.CharField(max_length=200, help_text='Digite o endereço do chefe da família', verbose_name='endereço')
    telefone1 = PhoneNumberField(help_text='Digite o telefone principal do chefe da família', verbose_name='telefone principal')
    telefone2 = PhoneNumberField(blank=True, null=True, help_text='Digite o telefone secundário do chefe da família (opcional)', verbose_name='telefone secundário')

    class Meta:
        ordering = ['chefe_da_familia']
        verbose_name = 'Família'
        verbose_name_plural = 'Famílias'

    def __str__(self):
        return self.chefe_da_familia

    def get_absolute_url(self):
        return reverse('detalhes-familia', args=[str(self.id)])


class IntegranteFamiliar(models.Model):
    chefe_da_familia = models.ForeignKey(Familia, on_delete=models.CASCADE, help_text='Selecione o chefe da família')
    nome = models.CharField(max_length=200, help_text='Digite o nome do integrante da família')
    cpf = models.CharField(max_length=11, blank=True, null=True, help_text='Digite o cpf do integrante da família')
    telefone = PhoneNumberField(blank=True, null=True, help_text='Digite o telefone do integrante da família (opcional)')

    class Meta:
        ordering = ['nome']
        verbose_name = 'Integrante de família'
        verbose_name_plural = 'Integrantes de famílias'

    def __str__(self):
        return self.chefe_da_familia.chefe_da_familia

    def get_absolute_url(self):
        return reverse('detalhes-integrante-familiar', args=[str(self.id)])


class Entidade(models.Model):
    nome_fantasia = models.CharField(max_length=200, help_text='Digite o nome-fantasia da entidade')
    cnpj = models.CharField(max_length=14, blank=True, null=True, help_text='Digite o cnpj da entidade')
    endereco = models.CharField(max_length=200, help_text='Digite o email da entidade', verbose_name = 'endereço')
    telefone = PhoneNumberField(blank=True, null=True, help_text='Digite o telefone da entidade (00)0 0000-0000 (Opcional)')
    email = models.EmailField(help_text='Digite o email da entidade')
    
    class Meta:
        ordering = ['nome_fantasia']
        verbose_name = 'Entidade'
        verbose_name_plural = 'Entidades'

    def __str__(self):
        return self.nome_fantasia

    def get_absolute_url(self):
        return reverse('detalhes-entidade', args=[str(self.id)])

class Representante(models.Model):
    entidade = models.ForeignKey(Entidade, on_delete=models.CASCADE, help_text='Selecione a entidade que o reprensentante irá representar')
    representante = models.ForeignKey(User, null=True, on_delete=models.CASCADE, help_text='Selecione o usuário representante')
    cpf = models.CharField(max_length=11, null=True, blank=True, help_text='Digite o cpf do integrante da família')

    class Meta:
        ordering = ['representante']
        verbose_name = 'Representante de entidade'
        verbose_name_plural = 'Representantes de entidades'
    
    def __str__(self):
        return self.representante.username

class Item(models.Model):
    nome = models.CharField(max_length=200, help_text='Digite o nome do item')

    class Meta:
        ordering = ['nome']
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

    def __str__(self):
        return self.nome


class Doacao(models.Model):
    chefe_da_familia = models.ForeignKey(Familia, on_delete=models.CASCADE, help_text='Selecione o chefe da família')
    representante = models.ForeignKey(User, on_delete=models.CASCADE, help_text='Selecione o usuário representante')
    data = models.DateField(help_text='Informe a data da doação')
    justificativa = models.TextField(max_length=200, blank=True, null=True, help_text='Digite a justificativa da doação')

    class Meta:
        ordering = ['data']
        verbose_name = 'Doação'
        verbose_name_plural = 'Doações'

    def __str__(self):
        return f"Doação para {self.chefe_da_familia.chefe_da_familia} feita em {self.data.strftime('%d/%m/%Y')}"

    def get_absolute_url(self):
        return reverse('detalhes-doacao', args=[str(self.id)])


class ItensDoacao(models.Model):
    doacao = models.ForeignKey(Doacao,null=True, on_delete=models.CASCADE, help_text='Selecione a doação')
    item = models.ForeignKey(Item, null=True, on_delete=models.CASCADE, help_text='Selecione o item')
    quantidade = models.PositiveIntegerField(null=True, help_text='Digite a quantidade do item selecionado')
    
    class Meta:
        ordering = []
        verbose_name = 'Item de doação'
        verbose_name_plural = 'Itens de doações'
    
    def __str__(self):
        return f"Item da doação para {self.doacao.chefe_da_familia.chefe_da_familia} feita em {self.doacao.data.strftime('%d/%m/%Y')}"
    
