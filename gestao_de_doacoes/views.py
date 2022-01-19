import json
from django.core import serializers
from datetime import date, timedelta
from django.core.paginator import Paginator
from gestao_de_doacoes.decorators import is_auth, allowed
from django.shortcuts import render, redirect, get_object_or_404
from gestao_de_doacoes.models import Familia, IntegranteFamiliar, Entidade, Item, Doacao, ItensDoacao
from authentication.models import Usuario
from gestao_de_doacoes.forms import FamilyForm, FamilyMemberForm, DonationForm

#dashboard.
@is_auth
@allowed(allowed_roles=['Usuário', 'Representante'], currentPage='dashboard')
def index(request):
    return redirect('dashboard')

@is_auth
@allowed(allowed_roles=['Usuário', 'Representante'], currentPage='dashboard')
def dashboard(request):
    users = Usuario.objects.filter(groups__name='Usuário')
    families = Familia.objects.all()
    entities = Entidade.objects.all()
    donations = Doacao.objects.all()

    end = date.today().replace(day=1) - timedelta(days=1)
    start = date.today().replace(day=1) - timedelta(days=end.day)
    
    context = {
      'user_count': users.count,
      'user_lastmonth:': users.filter(date_joined__range=[start, end]).count(),
      'family_count': families.count,
      'family_lastmonth': families.filter(data_cadastro__range=[start, end]).count(),
      'entity_count': entities.count,
      'entity_lastmonth': entities.filter(data_cadastro__range=[start, end]).count(),
      'donation_count': donations.count,
      'donation_lastmonth': donations.filter(data_cadastro__range=[start, end]).count(),
    }

    return render(request, 'dashboard/dashboard.html', context)

#family
@is_auth
@allowed(allowed_roles=['Usuário', 'Representante'], currentPage='family')
def family(request):
    family = Familia.objects.all()
    family_paginator = Paginator(family, 10)
    page_num = request.GET.get('page', 1)
    paginator = family_paginator.get_page(page_num)

    context = {
      'count': family_paginator.count,
      'paginator': paginator,
    }

    return render(request, 'family/family.html', context)

@is_auth
@allowed(allowed_roles=['Usuário', 'Representante'], currentPage='search_family')
def search_family(request):
    if 'search_term' in request.GET and request.GET['search_term']:   
        search_term = request.GET.get('search_term')

        families = Familia.objects.filter(chefe_da_familia__contains=search_term) | Familia.objects.filter(endereco__contains=search_term) | Familia.objects.filter(telefone1__contains=search_term)
        family_paginator = Paginator(families, 10)
        page_num = request.GET.get('page', 1)
        paginator = family_paginator.get_page(page_num)
        
        context = {
          'search_term': search_term,
          'count': family_paginator.count,
          'paginator': paginator,
        }

        return render(request, 'family/search_family.html', context)
    else:
        return redirect('family')

@is_auth
@allowed(allowed_roles=['Usuário', 'Representante'], currentPage='family_details')
def family_details(request, pk):
    family = get_object_or_404(Familia, pk=pk)
    members = IntegranteFamiliar.objects.filter(chefe_da_familia__exact=family.id)
    form = FamilyForm()
    member_form = FamilyMemberForm()
    
    if request.method == 'POST':
        if request.POST.get('update'):
            form = FamilyForm(request.POST)
            if form.is_valid():
                family.chefe_da_familia = request.POST.get('chefe_da_familia')
                family.cpf = request.POST.get('cpf')
                family.endereco = request.POST.get('endereco')
                family.telefone1 = request.POST.get('telefone1')
                family.telefone2 = request.POST.get('telefone2')
                family.save()
                return redirect('family_details', pk=pk)
        elif request.POST.get('remove'):
            family.delete()
            return redirect('family')
        elif request.POST.get('create_member'):
            member_form = FamilyMemberForm(request.POST)
            if member_form.is_valid():
              member_form.save()
              return redirect('family_details', pk=pk)

    context = {
      'family': family,
      'members': members,
      'form': form,
      'member_form': member_form,
    }
        
    return render(request, 'family/family_detail.html', context)

@is_auth
@allowed(allowed_roles=['Usuário'], currentPage='create_family')    
def create_family(request):
    form = FamilyForm()

    if request.method == 'POST':
        form = FamilyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/gestao/familias')

    context = {
      'form': form,
    }

    return render(request, 'family/create_family.html', context)

@is_auth
@allowed(allowed_roles=['Usuário', 'Representante'], currentPage='member_details')
def member_details(request, pk_family, pk_member):
    family = get_object_or_404(Familia, pk=pk_family)
    member = get_object_or_404(IntegranteFamiliar, pk=pk_member)
    form = FamilyMemberForm()

    if request.method == 'POST':
        if request.POST.get('update'):
            form = FamilyMemberForm(request.POST)
            if form.is_valid():
                member.nome = request.POST.get('nome')
                member.cpf = request.POST.get('cpf')
                member.telefone = request.POST.get('telefone')
                member.save()
                return redirect('member_details', pk_family=pk_family, pk_member=pk_member)
        elif request.POST.get('remove'):
            member.delete()
            return redirect('family_details', pk=pk_family)   
                
    context = {
      'family': family,
      'member': member,
      'form': form,
    }

    return render(request, 'family/member/member_detail.html', context)

#donation
@is_auth
@allowed(allowed_roles=['Usuário', 'Representante'], currentPage='donation')
def donation(request):
    donation = Doacao.objects.all()
    donation_paginator = Paginator(donation, 10)
    page_num = request.GET.get('page', 1)
    paginator = donation_paginator.get_page(page_num)

    context = {
      'count': donation_paginator.count,
      'paginator': paginator,
    }

    return render(request, 'donation/donation.html', context)

@is_auth
@allowed(allowed_roles=['Usuário', 'Representante'], currentPage='search_donation')
def search_donation(request):
    if 'search_term' in request.GET and request.GET['search_term']:   
        search_term = request.GET.get('search_term')

        donations = Doacao.objects.filter(chefe_da_familia__chefe_da_familia__contains=search_term) | Doacao.objects.filter(usuario__first_name__contains=search_term) | Doacao.objects.filter(data__contains=search_term) | Doacao.objects.filter(justificativa__contains=search_term)
        donation_paginator = Paginator(donations, 10)
        page_num = request.GET.get('page', 1)
        paginator = donation_paginator.get_page(page_num)
        
        context = {
          'search_term': search_term,
          'count': donation_paginator.count,
          'paginator': paginator,
        }

        return render(request, 'donation/search_donation.html', context)
    else:
        return redirect('donation')

@is_auth
@allowed(allowed_roles=['Usuário'], currentPage='donation')    
def create_donation(request):
    form_donation = DonationForm()
    families = Familia.objects.all()
    users = Usuario.objects.filter(groups__name='Usuário')
    items = Item.objects.all()

    if request.method == 'POST':
        form_donation = DonationForm(request.POST)
        savedModel = None
        if form_donation.is_valid():
            savedModel = form_donation.save()

        recieved_items = json.loads(request.POST.get('selectedItems'))

        for element in recieved_items:
            item_found = get_object_or_404(Item, pk=element['item'])
            ItensDoacao.objects.create(doacao=savedModel, item=item_found, quantidade=element['quantidade'])

        return redirect('donation')    
    
    context = {
      'form_donation': form_donation,
      'families': families,
      'items': items,
      'users': users,
    }

    return render(request, 'donation/create_donation.html', context)

@is_auth
@allowed(allowed_roles=['Usuário', 'Representante'], currentPage='donation') 
def donation_details(request, pk):
    donation = get_object_or_404(Doacao, pk=pk)
    families = Familia.objects.all()
    users = Usuario.objects.filter(groups__name='Usuário')
    items = Item.objects.all()
    items_donation = serializers.serialize('json', ItensDoacao.objects.filter(doacao=pk))
    form = DonationForm()
   
    if request.method == 'POST':
        if request.POST.get('update'):
            form = DonationForm(request.POST)
            if form.is_valid():
                donation.chefe_da_familia = get_object_or_404(Familia, pk=request.POST.get('chefe_da_familia'))
                donation.usuario = get_object_or_404(Usuario, pk=request.POST.get('usuario'))
                donation.data = request.POST.get('data')
                donation.justificativa = request.POST.get('justificativa')
                donation.save()

                recieved_items = json.loads(request.POST.get('selectedItems'))
                to_be_deleted = ItensDoacao.objects.filter(doacao=pk)

                for item in to_be_deleted:
                    item.delete()

                for element in recieved_items:
                    item_found = get_object_or_404(Item, pk=element['item'])
                    ItensDoacao.objects.create(doacao=donation, item=item_found, quantidade=element['quantidade'])

                return redirect('donation_details', pk=pk)
        elif request.POST.get('remove'):
            donation.delete() 
            return redirect('donation')   
                
    context = {
      'donation': donation,
      'form': form,
      'users': users,
      'items': items,
      'families': families,
      'items_donation': items_donation,
    }

    return render(request, 'donation/donation_detail.html', context)