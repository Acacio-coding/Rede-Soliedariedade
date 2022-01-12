from django.shortcuts import render
from django.shortcuts import redirect
from gestao_de_doacoes.models import Familia, IntegranteFamiliar, Entidade, Representante, Item, Doacao, ItensDoacao

# Create your views here.
def index(request):
    return redirect('gestao/dashboard/')

def dashboard(request):
    return render(request, 'dashboard.html')