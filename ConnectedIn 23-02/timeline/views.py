from django.shortcuts import *
from perfis.models import Perfil
# Create your views here.
from timeline.models import Post


def carregar_posts(request, id_perfil):
    perfil = Perfil.objects.get(id_perfil)
    posts = Post.objects.filter(usuario=perfil.user)
    posts_contatos = get_post_contatos(perfil.contatos)
    return render('timeline.html',
                  {'my_posts': posts,
                   'posts_contatos': posts_contatos})


def get_post_contatos(contatos):
    posts = []
    for contato in contatos:
        posts.append(Post.objects.filter(usuario=contato))
    return posts


def excluir_post(request, post_id):
    Post.objects.filter(id=post_id).delete()
    return redirect('self')
