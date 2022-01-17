from django.urls import path
from gestao_de_doacoes import views

urlpatterns = [
    path('', views.index),
    path('gestao/dashboard', views.dashboard, name='dashboard'),
    path('gestao/familias', views.family, name='family'),
    path('gestao/familias/pesquisa', views.search_family, name='search_family'),
    path('gestao/familias/nova', views.create_family, name='create_family'),
    path('gestao/familias/<int:pk>', views.family_details, name="family_details"),
    path('gestao/familias/<int:pk_family>/integrante/<int:pk_member>', views.member_details, name='member_details'),
    path('gestao/doacoes', views.donation, name='donation'),
    path('gestao/doacoes/pesquisa', views.search_donation, name='search_donation'),
    path('gestao/doacoes/nova', views.create_donation, name='create_donation'),
    path('gestao/doacoes/<int:pk>', views.donation_details, name="donation_details"),
]