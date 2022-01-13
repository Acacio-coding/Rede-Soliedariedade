from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from datetime import date, timedelta
from django.contrib.auth.models import User
from gestao_de_doacoes.models import Familia, IntegranteFamiliar, Entidade, Representante, Item, Doacao, ItensDoacao

# Create your views here.
def index(request):
    return redirect('gestao/dashboard')

def dashboard(request):
    families = Familia.objects.all()
    entities = Entidade.objects.all()
    donations = Doacao.objects.all()
    users = User.objects.all()

    end = date.today().replace(day=1) - timedelta(days=1)
    start = date.today().replace(day=1) - timedelta(days=end.day)
    
    context = {
      'family_count': families.count,
      'family_lastmonth': families.filter(data_cadastro__range=[start, end]).count(),
      'entity_count': entities.count,
      'entity_lastmonth': entities.filter(data_cadastro__range=[start, end]).count(),
      'donation_count': donations.count,
      'donation_lastmonth': donations.filter(data_cadastro__range=[start, end]).count(),
      'user_count': users.count,
    }

    return render(request, 'dashboard/dashboard.html', context)

def family(request):
    family = Familia.objects.all()
    family_paginator = Paginator(family, 10)
    page_num = request.GET.get('page')
    page = family_paginator.get_page(page_num)

    context = {
      'count': family_paginator.count,
      'page': page,
    }

    return render(request, 'family/family.html', context)

def family_details(request, pk):
    family = get_object_or_404(Familia, pk=pk)
    
    context = {
      'family': family,
    }

    return render(request, 'family/family_detail.html', context)

def search_family(request):
    if 'search_term' in request.GET and request.GET['search_term']:   
        search_term = request.GET.get('search_term')

        families = Familia.objects.filter(chefe_da_familia__contains=search_term) or Familia.objects.filter(endereco__contains=search_term) or Familia.objects.filter(telefone1__contains=search_term)
        family_paginator = Paginator(families, 10)
        page_num = request.GET.get('page')
        page = family_paginator.get_page(page_num)

        context = {
          'search_term': search_term,
          'count': family_paginator.count,
          'page': page,
        }

        return render(request, 'family/family_searched.html', context)
    else:
        return redirect('/gestao/familias')
    