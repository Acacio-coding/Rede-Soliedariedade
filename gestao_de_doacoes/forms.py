from django.forms import ModelForm
from gestao_de_doacoes.models import Familia, IntegranteFamiliar, Entidade, Representante, Item, Doacao, ItensDoacao

class FamilyForm(ModelForm):
    class Meta:
        model = Familia
        fields = '__all__'

class FamilyMemberForm(ModelForm):
    class Meta:
        model = IntegranteFamiliar
        fields = '__all__'