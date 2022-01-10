from django.shortcuts import render
from gestao_de_doacoes.models import Familia, IntegranteFamiliar, Entidade, Representante, Item, Doacao, ItensDoacao

# Create your views here.
def index(request):
    return render(request, 'index.html')