from django.shortcuts import render
from django.contrib.auth.models import User as U
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from projetos.models import *
# Create your views here.

PERFIL_LOGADO = None
PROJETOS = None

def index(request):
    mensagem = ""
    if request.method == "GET":
        return render(request,
                      "login.html",
                      {"mensagem": mensagem})

    if request.method == "POST":
        usuario = request.POST.get("username")
        senha = request.POST.get("senha")

        PERFIL_LOGADO = authenticate(username=usuario, password=senha)

        if PERFIL_LOGADO is not None:
            PROJETOS = Usuario_Projeto.objects.filter(usuario=PERFIL_LOGADO)
            login(request, usuario)
            return render(request,
                          "pagina_inicial.html",
                          {"PROJETOS": PROJETOS,
                           "perfil": PERFIL_LOGADO,
                           "mensagem": ""})
        else:
            mensagem = "Crendeciais nao encontradas"
            return render(request,
                          "login.html",
                          {"mensagem": mensagem})


def pagina_inicial(request):
    PROJETOS = Usuario_Projeto.objects.filter(usuario=PERFIL_LOGADO)
    return render(request,
                  "pagina_inicial.html",
                  {"projetos": PROJETOS,
                   "perfil": PERFIL_LOGADO,
                   "mensagem": ""})


def cadastrar_usuario(request):
    if request.method == "GET":
        return render(request,
                      "cadastro.html")
    if request.method == "POST":
        usuario = request.POST.get("username")
        senha = request.POST.get("password")
        email = request.POST.get("email")

        novo = U.objects.create_user(username=usuario, password=senha)

        PERFIL_LOGADO = Perfil.objects.create(usuario=novo, email=email)
        mensagem = "Seu cadastro foi realizado com sucesso"
        PROJETOS = Usuario_Projeto.objects.filter(usuario=PERFIL_LOGADO)
        return render(request,
                      "pagina_inicial.html",
                      {"perfil": PERFIL_LOGADO,
                       "projetos": PROJETOS,
                       "mensagem": mensagem})


@login_required
def criar_projeto(request):
    if request.method == "GET":
        return render(request,
                      "criar_projeto.html")
    if request.method == "POST":
        descricao = request.POST.get("descricao")
        dt_inicial = request.POST.get("dt_inicial")
        prazo = request.POST.get("prazo_previsto")

        Projeto.objects.create(descricao=descricao,
                               data_inicial=dt_inicial,
                               prazo_previsto=prazo,
                               administrador=PERFIL_LOGADO,
                               membros=PERFIL_LOGADO).save()
        PROJETOS = Usuario_Projeto.objects.filter(usuario=PERFIL_LOGADO)
        return render(request,
                      "pagina_inicial.html",
                      {"perfil": PERFIL_LOGADO,
                       "projetos": PROJETOS,
                       "mensagem": "Projeto criado com sucesso"})

@login_required
def excluir_projeto(request, projeto_id):
    projeto = Usuario_Projeto.objects.get(id=projeto_id)
    try:
        projeto.delete()
        mensagem = "Projeto excluido com sucesso"
        PROJETOS = Usuario_Projeto.objects.filter(usuario=PERFIL_LOGADO)
    except:
        mensagem = "Não possivel excluir o projeto, por favor tente novamente"
    return render(request,
                  "pagina_inicial.html",
                  {"mensagem:": mensagem,
                   "perfil": PERFIL_LOGADO,
                   "projetos": PROJETOS})