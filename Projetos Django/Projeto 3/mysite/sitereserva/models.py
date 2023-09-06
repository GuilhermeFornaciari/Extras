from django.db import models

# Create your models here.
class Apartamento(models.Model):
    categoria = models.CharField(max_length=200)
    precoDia = models.FloatField()
    capacidade = models.IntegerField()

    imagem1 = models.ImageField()
    imagem2 = models.ImageField()
    imagem3 = models.ImageField()
    imagem4 = models.ImageField()

class Carro(models.Model):
    categoria = models.CharField(max_length=200)
    precoDia = models.FloatField()
    capacidade = models.IntegerField()

    imagem1 = models.ImageField()
    imagem2 = models.ImageField()
    imagem3 = models.ImageField()
    imagem4 = models.ImageField()



