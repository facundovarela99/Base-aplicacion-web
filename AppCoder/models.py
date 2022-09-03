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
    
    def __str__ (self):
        return self.nombre+" "+str(self.comision)

class Estudiante(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    
    def __str__ (self):
        return self.nombre+" "+self.apellido

class Profesor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__ (self):
        return self.nombre+" "+self.apellido

class Entregable(models.Model):
    nombre=models.CharField(max_length=50)
    fecha_entrega=models.DateField()
    entregado=models.BooleanField()


