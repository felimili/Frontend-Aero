from django.db import models

# Create your models here.

class usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    mail = models.EmailField(default='a@a.com.ar')
    password = models.CharField(max_length=8) 
    def __str__(self):
        return self.nombre


class avion(models.Model):
    id = models.AutoField(primary_key=True)
    modelo = models.CharField(max_length=30)
    matricula = models.CharField(max_length=6)

    def __str__(self):
        return self.modelo

class vuelo(models.Model):
    apellido= models.CharField(max_length=30)
    nombre= models.CharField(max_length=30)
    matricula= models.CharField(max_length=6)
    inicio= models.DateTimeField
    fin= models.DateTimeField
    origen= models.CharField(max_length=5)
    destino= models.CharField(max_length=5)
    tiempoVuelo = models.FloatField

    def __str__(self):
        return self.modelo
    




