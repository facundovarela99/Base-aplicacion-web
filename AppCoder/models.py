import email
from django.db import models

# Create your models here.

class Familiares(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    fecha_nacimiento=models.DateField()

class Curso(models.Model):
    nombre=models.CharField(max_length=50)
    comision=models.IntegerField()

class Estudiante(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

class Profesor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

class Entregable(models.Model):
    nombre=models.CharField(max_length=50)
    fecha_entrega=models.DateField()
    entregado=models.BooleanField()


