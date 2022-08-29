from django.shortcuts import render
from .models import Familiares
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def familiar_1_html(request):
    familiar_1=Familiares(nombre='Edgardo', apellido='Varela', fecha_nacimiento='1963-05-05')
    familiar_1.save()
    familiar_01={'nombre':familiar_1.nombre, 'apellido':familiar_1.apellido, 'fecha_nacimiento':familiar_1.fecha_nacimiento}
    #cargo template
    plantilla=loader.get_template('template.html')
    #renderizo contexto (que es un diccionario)
    documento=plantilla.render(familiar_01)
    return HttpResponse(documento)

def familiar_2_html(request):
    familiar_2=Familiares(nombre='Norma', apellido='Alagna', fecha_nacimiento='1965-06-10')
    familiar_2.save()
    familiar_02={'nombre':familiar_2.nombre, 'apellido':familiar_2.apellido, 'fecha_nacimiento':familiar_2.fecha_nacimiento}
    plantilla=loader.get_template('template.html')
    documento=plantilla.render(familiar_02)
    return HttpResponse(documento)

def familiar_3_hmtl(request):
    familiar_3=Familiares(nombre='Gaspar Rodolfo', apellido='Alagna', fecha_nacimiento='1932-01-11')
    familiar_3.save()
    familiar_03={'nombre':familiar_3.nombre, 'apellido':familiar_3.apellido, 'fecha_nacimiento':familiar_3.fecha_nacimiento} 
    plantilla=loader.get_template('template.html')
    documento=plantilla.render(familiar_03)
    return HttpResponse(documento)



