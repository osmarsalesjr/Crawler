from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    usuario = models.OneToOneField(User, related_name="perfil",
                                   on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return "User: %S | Email: %s " % (self.username, self.email)


class Projeto(models.Model):
    descricao = models.CharField(max_length=255)
    data_inicial = models.DateField()
    prazo_previsto = models.DateField()
    administrador = models.ForeignKey('Perfil',
                                      related_name="administradores",
                                      on_delete=models.CASCADE)
    membros = models.ManyToManyRel('Perfil', through='Usuario_Projeto', to="")
    def __str__(self):
        return "Projeto: %s | Dt. Inicial: %s" % (self.descricao, self.data_inicial)


class Usuario_Projeto(models.Model):
    usuario = models.ForeignKey('Perfil',
                                related_name='usuarios',
                                on_delete=models.CASCADE)
    projeto = models.ForeignKey('Projeto',
                                related_name='grupos',
                                on_delete=models.CASCADE)
    data_entrada = models.DateField()
