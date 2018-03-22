from django.db import models


# Create your models here.
class Empresa(models.Model):
    cnpj = models.CharField(max_length=14)
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    telefone = models.CharField(max_length=30)
    senha_acesso = models.CharField(max_length=255)

    def __str__(self):
        return "Nome: %s | E-mail: %s" % (self.nome, self.email)


class Cargo(models.Model):
    descricao_cargo = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao_cargo


class Funcionario(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    telefone = models.CharField(max_length=255)
    senha_acesso = models.CharField(max_length=255)
    cargo_funcionario = models.ForeignKey('Cargo',
                                             related_name='cargos',
                                             on_delete=models.CASCADE)
    empresa_funcionario = models.ForeignKey('Empresa',
                                            related_name='funcionarios',
                                            on_delete=models.CASCADE)

    def __str__(self):
        return "Nome: %s | E-mail: %s" % (self.nome, self.email)