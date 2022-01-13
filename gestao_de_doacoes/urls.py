from django.urls import path
from gestao_de_doacoes import views

urlpatterns = [
    path('', views.index),
    path('gestao/dashboard', views.dashboard, name='dashboard'),
    path('gestao/familias', views.family, name='family'),
    path('gestao/familias/<int:pk>', views.family_details, name="family_details"),
    path('gestao/familias/pesquisa', views.search_family, name="search_family"),
]