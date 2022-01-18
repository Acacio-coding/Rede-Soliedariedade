from django.forms import ModelForm
from django.contrib.auth import forms
from gestao_de_doacoes.models import Familia, IntegranteFamiliar, Entidade, Usuario, Item, Doacao, ItensDoacao


class FamilyForm(ModelForm):
    class Meta:
        model = Familia
        fields = '__all__'


class FamilyMemberForm(ModelForm):
    class Meta:
        model = IntegranteFamiliar
        fields = '__all__'


class DonationForm(ModelForm):
    class Meta:
        model = Doacao
        fields = '__all__'
