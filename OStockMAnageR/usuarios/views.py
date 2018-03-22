from django.shortcuts import render, redirect
from django.contrib.auth import *
from random import randint
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail

from usuarios.models import *

PERFIL_LOGADO = None


# Create your views here.

def pagina_inicial(request):
    return render(request,
                  "pagina_inicial.html",
                  {"perfil_logado": PERFIL_LOGADO})


def login_sistema(request):

    if not User.objects.exists():
        User.objects.create_user('admin', 'admin@admin.com', '59914010').save()

    if request.method == "GET":
        return render(request,
                      "login.html")

    if request.method == "POST":
        email = request.POST.get("email_empresa")
        senha = request.POST.get("senha")

        PERFIL_LOGADO = authenticate(email = email, senha_acesso = senha)

        '''if Empresa.objects.filter(email=email, senha_acesso=senha).exists():
            PERFIL_LOGADO = Empresa.objects.filter(email=email, senha_acesso=senha)

        if Funcionario.objects.filter(email=email, senha_acesso=senha).exists():
            PERFIL_LOGADO = Funcionario.objects.filter(email=email, senha_acesso=senha)'''

        if PERFIL_LOGADO != None:
            login(request, PERFIL_LOGADO)
            return pagina_inicial(request)
        else:
            return render(request,
                          "sessao_mensagem.html",
                          {"mensagem": "Credenciais não encontradas! Por favor tente logar novamente."})


##@login_required
def registrar_empresa(request):
    if request.method == "GET":
        return render(request, "registrar_empresa.html")

    if request.method == "POST":
        cnpj = request.POST.get("cnpj")
        nome = request.POST.get("nome_empresa")
        email = request.POST.get("email_empresa")
        telefone = request.POST.get("telefone")
        senha = request.POST.get("senha")

        if Empresa.objects.filter(cnpj=cnpj, email=email).exists():
            return render(request,
                          "sessao_mensagem.html",
                          {"mensagem": "A empresa já esta cadastrada!"})
        try:
            Empresa.objects.create(cnpj=cnpj, nome=nome,
                                   email=email, telefone=telefone,
                                   senha_acesso=senha)
        except:
            return render(request,
                          "sessao_mensagem.html",
                          {"mensagem": "Ocorreu um erro na confirmação do cadastro, por favor tente novamente"})
        return render(request,
                      "sessao_mensagem.html",
                      {"mensagem": "O cadastro da sua empressa foi realizado com sucesso."})


def recuperar_senha(request):

    if request.method == "GET":
        return render(request,
                      "recuperar_senha.html")

    if request.method == "POST":
        email = request.POST.get("email")
        opcao = request.POST.get("perfil")
        perfil = None


        if Empresa.objects.filter(email=email).exists():
            perfil = Empresa.objects.get(email=email)

        if perfil is None and Funcionario.objects.filter(email=email).exists():
            perfil = Funcionario.objects.get(email=email)

        if perfil is None:
            return render(request,
                          "sessao_mensagem.html",
                          {"mensagem": "E-mail não encotrado, por favor verifique e tente novamente"})
        else:

            numeracao = randint(100000, 999999)
            texto_email = "Olá %s,\nClique no link abaixo para atualizar a senha do seu cadastro."
            texto_email += "\nLink: http://localhost:8000/atualizar_senha/%s/%d/%d" % (opcao, perfil.id, numeracao)

            try:
                send_mail(
                    "OStockMAnageR - Recuperação de Senha",
                    texto_email,
                    'osmarsalesjr@gmail.com',
                    [email],
                    fail_silently=False
                )
            except:
                return render(request,
                              "sessao_mensagem.html",
                              {"mensagem": "Erro na conexão, por favor tente novamente."})

            return render(request,
                          "sessao_mensagem.html",
                          {"mensagem": "O link de recuperação foi enviado para seu e-mail, por favor confira-o."})


def atualizar_senha_empresa(request, perfil_id, numeracao):

    if request.method == "GET":
        return render(request,
                      "atualizar_senha.html",
                      {"codigo":numeracao})

    if request.method == "POST":
        perfil = Empresa.objects.get(id=perfil_id)
        nova_senha = request.POST.get("nova_senha")
        perfil.senha_acesso = nova_senha
        perfil.save()

        return render(request,
                      "sessao_mensagem.html",
                      {"mensagem": "A sua senha foi atualizada com sucesso."})
    return render(request,
                  "sessao_mensagem",
                  {"mensagem": "Houve um erro na recuperação de senha, por favor tente novamente"})



def atualizar_senha_funcionario(request, perfil_id, numeracao):

    if request.method == "GET":
        return render(request,
                      "atualizar_senha.html",
                      {"codigo":numeracao})

    if request.method == "POST":
        perfil = Funcionario.objects.get(id=perfil_id)
        nova_senha = request.POST.get("nova_senha")
        perfil.senha_acesso = nova_senha
        perfil.save()

        return render(request,
                      "sessao_mensagem.html",
                      {"mensagem": "A sua senha foi atualizada com sucesso."})
    return render(request,
                  "sessao_mensagem",
                  {"mensagem": "Houve um erro na recuperação de senha, por favor tente novamente"})