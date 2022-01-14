from unicodedata import name
from django.urls import path

from .views import (
    profile_Test_view,
    MyProfileView,
    MainPageView,
    MyContasData,
    MyReceitasData,
    ExpecificContaView,
    CriarContaView,
    NewReceitaView
    
)

app_name = 'profiles'

urlpatterns = [
    path('test/', profile_Test_view, name='test_profile'),
    path('', MyProfileView, name='my-profile-view'),
    path('new-conta/', CriarContaView, name="criar-conta"),
    path('contas-json/', MyContasData.as_view(), name='my-contas-data'),
    path('receitas-json/<str:conta>', MyReceitasData, name='my-receitas-data'),
    path('conta/<str:conta>', ExpecificContaView, name='conta'),
    path('conta/<str:conta>/new-receita', NewReceitaView, name="new-receita")
]