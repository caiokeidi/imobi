from django.db import models
from django.contrib.auth.models import User

class Imoveis(models.Model):
    corretor = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    cliente = models.CharField(max_length=50)

    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    rua = models.CharField(max_length=50)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    tipo_negocio = models.CharField(max_length=20)
    tipo_imovel = models.CharField(max_length=25)
    valor_aluguel = models.FloatField(blank=True, null=True)
    valor_venda = models.FloatField(blank=True, null=True)
    valor_iptu = models.FloatField(blank=True, null=True)
    valor_condominio = models.FloatField(blank=True, null=True)

    area = models.IntegerField()
    quartos = models.IntegerField()
    suites = models.IntegerField()
    banheiros = models.IntegerField()
    vagas = models.IntegerField()
    andar = models.IntegerField(blank=True, null=True)
    metro_proximo = models.BooleanField(default=False)
    mobiliado = models.BooleanField(default=False) 

    descricao = models.TextField(max_length=1500)

    publicado = models.BooleanField()

class imagens(models.Model):
    imoveis = models.ForeignKey(Imoveis, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)


    


    
