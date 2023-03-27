from django.db import models

# Create your models here.

class Task(models.Model):
    subject = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.subject

class Generos(models.Model):
    id = models.AutoField(primary_key=True)
    generos = models.CharField(max_length=100)

class Usuarios (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
    generos = models.ForeignKey(Generos,on_delete= models.PROTECT,default=False )