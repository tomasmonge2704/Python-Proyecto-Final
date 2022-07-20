from django.db import models

# Create your models here.
class Familiares(models.Model):
    nombre= models.CharField(max_length=40)
    relacionFamiliar= models.CharField(max_length=40)

class Curso(models.Model):
    nombre= models.CharField(max_length=40)
    camada= models.CharField(max_length=40)

class Post(models.Model):
    fecha = models.CharField(max_length=40)
    titulo = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=40)
