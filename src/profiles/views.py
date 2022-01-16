from django.shortcuts import redirect, render
from .models import Conta, Profile, Receita
from django.views.generic import TemplateView, View
from django.http import JsonResponse, request, response, HttpResponseRedirect
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse
import datetime

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
        return HttpResponseRedirect(reverse('profiles:my-profile-view'))
    else:
        return render(request, 'profiles/my_profile.html')
    
def ExpecificContaView(request, conta):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('profiles:my-profile-view'))
    else:
        return render(request, 'profiles/conta.html', {"conta":conta})

def FiltroContaView(request, conta):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('profiles:my-profile-view'))
    else:
        if request.method == 'POST':
            inicial = request.POST['Inicial']
            final = request.POST['Final']
            checkbox = request.POST.get('checkbox', False)
            filtro = request.POST['filtro']
            return HttpResponseRedirect(reverse('profiles:filtro-conta-pagina', kwargs={'conta': conta})+f'?dataInicio={inicial}&dataFinal={final}&checkbox={checkbox}&descricao={filtro}')
        return render(request, 'profiles/filtro.html', {"conta":conta})
    
def FiltroReceitaView(request, conta):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('profiles:my-profile-view'))
    else:
        inicial = request.GET.get('dataInicio', '')
        final = request.GET.get('dataFinal', '')
        checkbox = request.GET.get('checkbox', '')
        filtro = request.GET.get('descricao', '')
        return render(request, 'profiles/filtro_receitas_pagina.html', {"conta":conta, "dataInicio": inicial, "dataFinal": final, "checkbox":checkbox, "descricao":filtro})
    
def TransferContaView(request, conta):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('profiles:my-profile-view'))
    else:
        if request.method == 'POST':
            nome = request.POST["nome"]
            valor = request.POST["valor"]
            
            if nome == conta or int(valor) <= 0:
                return HttpResponseRedirect(reverse('profiles:my-profile-view'))
            
            conta_receber_dinheiro = Conta.objects.filter(nome=nome, autor=request.user.perfil).first()
            conta_debitar_dinheiro = Conta.objects.filter(nome=conta, autor=request.user.perfil).first()
            
            conta_debitar_dinheiro.saldo -= int(valor)
            conta_debitar_dinheiro.save()
            
            conta_receber_dinheiro.saldo += int(valor)
            conta_receber_dinheiro.save()
            
            new_receita = Receita(valor=valor, autor=conta_receber_dinheiro, descricao=f"Transferencia de {conta_debitar_dinheiro}", dataPagamento=datetime.date.today())
            new_receita.save()
            
            new_receita = Receita(valor=-(int(valor)), autor=conta_debitar_dinheiro, descricao=f"Transferencia para {conta_receber_dinheiro}", dataPagamento=datetime.date.today())
            new_receita.save()
            
            
            return HttpResponseRedirect(reverse('profiles:my-profile-view'))
        return render(request, 'profiles/transfer_conta.html', {"conta":conta})
    
    
def NewReceitaView(request, conta):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('profiles:my-profile-view'))
    else:
        if request.method == 'POST':
            descricao = request.POST["descricao"]
            saldo = request.POST["saldo"]
            dataPagamento = request.POST["dataPagamento"]
            
            ano = dataPagamento[6:]
            mes = dataPagamento[3:5]
            dia = dataPagamento[:2]
            
            dataPagamento = datetime.date(int(ano), int(mes), int(dia))
            
            
            conta = Conta.objects.filter(autor=request.user.perfil, nome=conta).first()
            
            new_receita = Receita(valor=saldo, autor=conta, descricao=descricao, dataPagamento=dataPagamento)
            new_receita.save()
            
            conta.saldo += int(saldo)
            conta.save()
            
            return HttpResponseRedirect(reverse('profiles:my-profile-view'))
        return render(request, 'profiles/new_receita.html', {"conta":conta})
    
def CriarContaView(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('profiles:my-profile-view'))
    else:
        if request.method == 'POST':
            nome = request.POST["nome"]
            instituicao = request.POST["instituicao"]
            saldo = request.POST["saldo"]
            tipo = request.POST["tipo"]
            
            if nome == "" or instituicao == "" or tipo == "":
                return HttpResponseRedirect(reverse('profiles:criar-conta'))
            
            if Conta.objects.filter(nome=nome).first() != None:
                return HttpResponseRedirect(reverse('profiles:criar-conta'))
            else:
                nova_conta = Conta(nome=nome, instituicao=instituicao, saldo=saldo, tipo=tipo,autor=request.user.perfil)
                nova_conta.save()

                nova_receita = Receita(valor=saldo, autor=nova_conta, descricao=f"Criação de Conta", dataPagamento=datetime.date.today())
                nova_receita.save()
                return HttpResponseRedirect(reverse('profiles:my-profile-view'))
        return render(request, 'profiles/new_conta.html')
    
def EditarContaView(request, conta):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('profiles:my-profile-view'))
    else:
        if request.method == "POST":
            nome = request.POST["nome"]
            instituicao = request.POST["instituicao"]
            tipo = request.POST["tipo"]
            
            conta_editar = Conta.objects.filter(nome=conta,autor=request.user.perfil).first()
            
            conta_editar.nome = nome
            conta_editar.instituicao = instituicao
            conta_editar.tipo = tipo
            conta_editar.save()
            
            
            return HttpResponseRedirect(reverse('profiles:my-profile-view'))
        return render(request, 'profiles/edit_conta.html', {"conta":conta})
    
def MyReceitasData(request, conta):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('profiles:my-profile-view'))
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
                lista.append(receitadict)
                
            
            return JsonResponse({"conta" : contadata, 
                                 "receitas" : lista})

def MyFiltroReceitasData(request, conta):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('profiles:my-profile-view'))
    else:
        dataInicioGet = request.GET.get('dataInicio', '')
        dataFinalGet = request.GET.get('dataFinal', '')
        checkboxGet = request.GET.get('checkbox', '')
        descricaoGet = request.GET.get('descricao', '')
        
        profile = Profile.objects.get(user=request.user)
        conta_pedinte = Conta.objects.filter(autor=profile, nome=conta).first()
        
        ano = dataInicioGet[6:]
        mes = dataInicioGet[3:5]
        dia = dataInicioGet[:2]
        
        dataInicioGetFormatado = datetime.date(int(ano), int(mes), int(dia))
        
        print(dataInicioGetFormatado)
        
        ano = dataFinalGet[6:]
        mes = dataFinalGet[3:5]
        dia = dataFinalGet[:2]
        
        dataFinalGetFormatado = datetime.date(int(ano), int(mes), int(dia))

        if checkboxGet == "True":
            qs = Receita.objects.filter(autor=conta_pedinte,descricao=descricaoGet, dataPagamento__range=(dataInicioGetFormatado,dataFinalGetFormatado))
        else:
            qs = Receita.objects.filter(autor=conta_pedinte, dataPagamento__range=(dataInicioGetFormatado,dataFinalGetFormatado))
        
        lista = []
        for i in qs:
            receitasdict = {}
            receitasdict["descricao"] = i.descricao
            receitasdict["valor"] = i.valor
            receitasdict["criado"] = i.created
            receitasdict["dataPagamento"] = i.dataPagamento
            lista.append(receitasdict)
            
        return JsonResponse({"data" : lista})


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
        
        