from django.db import models
# Create your models here.
class Categoria(models.Model):
    descricao_categoria = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao_categoria


class Marca(models.Model):
    cnpj = models.CharField(max_length=14)
    sigla_nome_marca = models.CharField(max_length=255)
    descricao_marca = models.CharField(max_length=255)

    def __str__(self):
        return self.sigla_nome_marca

class Fornecedor(models.Model):
    nome_fornecedor = models.CharField(max_length=255)
    email_fornecedor = models.EmailField(max_length=255)
    telefone_fornecedor = models.CharField(max_length=30)

    def __str__(self):
        return "Nome: %s | E-mail: %s | Telefone: %s" % (self.nome_fornecedor,
                     self.email_fornecedor,
                     self.telefone_fornecedor)


class Produto(models.Model):
    descricao_produto = models.CharField(max_length=255)
    preco_unitario = models.FloatField()
    preco_atacado = models.FloatField()
    qtd_minima = models.IntegerField()
    qtd_estoque = models.IntegerField()
    categoria_produto = models.ForeignKey('Categoria',
                                          related_name='categorias',
                                          on_delete=models.CASCADE)
    marca_produto = models.ForeignKey('Marca',
                                      related_name='marcas',
                                      on_delete=models.CASCADE)
    fornecedor_produto = models.ForeignKey('Fornecedor',
                                           related_name='fornecedores',
                                           on_delete=models.CASCADE)

    def __str__(self):
        return "Descricao: %s | Preco unit.: R$ %.2f | Qtd. estoque: %d" % (self.descricao_produto,
                     self.preco_unitario,
                     self.qtd_estoque)

