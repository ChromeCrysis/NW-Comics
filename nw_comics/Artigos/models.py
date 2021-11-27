from django.db import models
from django.db.models.deletion import CASCADE
from Login.models import Usuarios

# Create your models here.

class Artigos(models.Model):
    titulo = models.TextField()
    genero = models.CharField(max_length=255)
    resumo = models.TextField()
    capa = models.ImageField()
    usuario = models.ForeignKey('auth.User', on_delete=CASCADE)

class Capitulos(models.Model):
    artigo = models.ForeignKey(Artigos, on_delete=CASCADE)
    texto = models.TextField()
    imagem1 = models.ImageField()
    imagem2 = models.ImageField()
    imagem3 = models.ImageField()
