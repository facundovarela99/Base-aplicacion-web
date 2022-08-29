from django.shortcuts import render
from .models import Curso, Familiares
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def familiar(request):
    familiar_1=Familiares(nombre='Edgardo', apellido='Varela', fecha_nacimiento='1963-05-05')
    familiar_2=Familiares(nombre='Norma', apellido='Alagna', fecha_nacimiento='1965-06-10')
    familiar_3=Familiares(nombre='Gaspar Rodolfo', apellido='Alagna', fecha_nacimiento='1932-01-11')
    familiar_1.save()
    familiar_2.save()
    familiar_3.save()
    texto=f'Familiares: Nombre: {familiar_1.nombre} Apellido: {familiar_1.apellido} Fecha nacimiento: {familiar_1.fecha_nacimiento}'
    return HttpResponse(texto)

def familiahtml(request):
    familiar_1=Familiares(nombre='Edgardo', apellido='Varela', fecha_nacimiento='1963-05-05')
    familiar_2=Familiares(nombre='Norma', apellido='Alagna', fecha_nacimiento='1965-06-10')
    familiar_3=Familiares(nombre='Gaspar Rodolfo', apellido='Alagna', fecha_nacimiento='1932-01-11')
    familiar_1.save()
    familiar_2.save()
    familiar_3.save()
    lista=[familiar_1, familiar_2, familiar_3]
    diccionario={'lista':lista}
    #cargo template
    plantilla=loader.get_template('template.html')
    #renderizo contexto (que es un familiar)
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)


def curso(request):
    curso=Curso(nombre='Python', comision=31105)
    curso_2=Curso(nombre='lengua', comision=2)
    curso_3=Curso(nombre='Matematica', comision=3)
    curso.save()
    curso_2.save()
    curso_3.save()
    texto=f'Cursos Creados: nombre: {curso.nombre} comision: {curso.comision}'
    return HttpResponse(texto)
