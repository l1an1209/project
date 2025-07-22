from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=60)
    email = models.EmailField(max_length=30)
    cidade = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    contato = models.CharField(max_length=30)
    cep = models.CharField(max_length=25)
    
    def str (self):
        return "{}({})".format(self.nome, self.email)

class Produto(models.Model):
    descricao = models.CharField(max_length=50, verbose_name='descrição')
    marca_produto = models.CharField(max_length=100)
    detalher_produto = models.CharField(max_length=50)
    data_chegada = models.DateField()
    quantidade = models.PositiveIntegerField(default=0) 
    preco_unitario = models.IntegerField(null=True)
    valor = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # calcula o valor do produto
        self.valor = self.quantidade * self.preco_unitario
        super(Produto, self).save(*args, **kwargs)


    

class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    data_venda = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.subtotal = self.quantidade * self.preco_unitario
        super().save(*args, **kwargs)