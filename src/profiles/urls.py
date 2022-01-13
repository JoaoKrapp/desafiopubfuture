from django.urls import path

from .views import (
    profile_Test_view,
    MyProfileView,
    MainPageView,
    MyContasData,
    MyReceitasData,
    ExpecificContaView,
    CriarContaView
    
)

app_name = 'profiles'

urlpatterns = [
    path('', MainPageView.as_view(), name='index'),                  
    path('test/', profile_Test_view, name='test_profile'),
    path('my/', MyProfileView, name='my-profile-view'),
    path('my/new-conta/', CriarContaView, name="criar-conta"),
    path('my-contas-json/', MyContasData.as_view(), name='my-contas-data'),
    path('my-receitas-json/<str:conta>', MyReceitasData, name='my-receitas-data'),
    path('my/conta/<str:conta>', ExpecificContaView, name='conta')
]