from django.urls import path
from gestao_de_doacoes import views

urlpatterns = [
    path('', views.index),
    path('gestao/dashboard/', views.dashboard, name='dashboard'),
]