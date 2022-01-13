from django.shortcuts import redirect, render
from .models import Conta, Profile
from django.views.generic import TemplateView, View
from django.http import JsonResponse, request, response, HttpResponseRedirect
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse

# Create your views here.
# TODO 
# Backend : Fazer o botão de exluir post
# Backend : Fazer o botão de follow do modal funcionar
# Backend : Fazer o botão de random page funcionar
# Frontend : Estilizar os accounts /base.html



def profile_Test_view(request):
    if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('mainpage:index'))
    profile = Profile.objects.get(user=request.user)
    return render(request, 'profiles/test_profile.html', {'profile':profile, 'testando': 'testaaaaaa'})

def MyProfileView(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('profiles:index'))
    else:
        return render(request, 'profiles/my_profile.html')
    
def ExpecificContaView(request, conta):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('profiles:index'))
    else:
        return render(request, 'profiles/conta.html', {"conta":conta})
    
def CriarContaView(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('profiles:index'))
    else:
        if request.method == 'POST':
            nome = request.POST["nome"]
            instituicao = request.POST["instituicao"]
            saldo = request.POST["saldo"]
            tipo = request.POST["tipo"]
            
            if nome == "" or instituicao == "" or tipo == "":
                return HttpResponseRedirect(reverse('profiles:criar-conta'))
            
            nova_conta = Conta(nome=nome, instituicao=instituicao, saldo=saldo, tipo=tipo,autor=request.user.perfil)
            nova_conta.save()
            return HttpResponseRedirect(reverse('profiles:my-profile-view'))
        
        return render(request, 'profiles/new_conta.html')
    
def MyReceitasData(request, conta):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('profiles:index'))
    else:
        profile = Profile.objects.get(user=request.user)
        conta = Conta.objects.filter(nome=conta,autor=profile).first()
        
        if conta != None:
            contadata = {
                "nome" : conta.nome,
                "instituicao" : conta.instituicao,
                "tipo" : conta.tipo,
                "saldo" : conta.saldo
            }

            lista = []
            for receita in conta.get_receitas():
                receitadict = {}
                receitadict["descricao"] = receita.descricao
                receitadict["valor"] = receita.valor
                receitadict["criado"] = receita.created
                receitadict["dataPagamento"] = receita.dataPagamento
                receitadict["dataPagamentoEsperado"] = receita.dataPagamentoEsperado
                lista.append(receitadict)
                
            
            return JsonResponse({"conta" : contadata, 
                                 "receitas" : lista})


class MainPageView(TemplateView):
    template_name = 'profiles/main.html'
    
class MyContasData(View):
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('mainpage:index'))
        else:
            profile = Profile.objects.get(user=self.request.user)
            qs = profile.get_contas_list()
            lista = []
            for conta in qs:
                contadict = {}
                contadict["nome"] = conta.nome
                contadict["instituicao"] = conta.instituicao
                contadict["tipo"] = conta.tipo
                contadict["saldo"] = conta.saldo
                lista.append(contadict)
                
            return JsonResponse({'contas' : lista})
        
        