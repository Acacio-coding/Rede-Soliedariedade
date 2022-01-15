from django.forms import ModelForm
from django.contrib.auth import forms
from gestao_de_doacoes.models import Familia, IntegranteFamiliar, Entidade, Usuario, Item, Doacao, ItensDoacao

class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Usuario


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Usuario


class FamilyForm(ModelForm):
    class Meta:
        model = Familia
        fields = '__all__'


class FamilyMemberForm(ModelForm):
    class Meta:
        model = IntegranteFamiliar
        fields = '__all__'