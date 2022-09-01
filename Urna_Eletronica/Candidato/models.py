from distutils.command.upload import upload
from msilib.schema import File
from turtle import update
from django.db import models


class Partido(models.Model):
    nome = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    
    def __str__(self):
        return self.nome
    
class Resultado(models.Model):
    resultado = models.IntegerField(
        editable=True,
    )
    
    def __str__(self):
        return self.nome
    
class Candidato(models.Model):
    nome = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )
    foto = models.ImageField(
        upload_to="static"
    )
    numero = models.IntegerField(
    )
    partido = models.ForeignKey(
        Partido,
        on_delete=models.PROTECT,
    )
    resultado = models.IntegerField(
        editable=True,
    )
    
    def __str__(self):
        return self.nome