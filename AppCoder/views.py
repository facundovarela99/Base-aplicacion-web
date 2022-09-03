from django.shortcuts import render
from .forms import CursoForm, ProfeForm
from .models import *
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

def curso(request):
    curso=Curso(nombre='AWS', comision=3)
    curso_2=Curso(nombre='Lengua', comision=4)
    curso_3=Curso(nombre='Python', comision=6)
    curso.save()
    curso_2.save()
    curso_3.save()

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def cursos(request):
    return render(request, 'AppCoder/cursos.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')

def estudiantecito(request):
    estudiantecito=Estudiante(nombre='CECINIO', apellido='Gonzalez')
    return render(request, 'AppCoder/estudiantecito.html')

"""def estudiantecin(request):
    estudiantecin=Estudiante(nombre='Roma', apellido='Benitez', email='roma@roma.com')
    estudiantecin.save()
    estudiantecin_0={'nombre':estudiantecin.nombre, 'apellido':estudiantecin.apellido, 'email':estudiantecin.email}
    plantilla=loader.get_template('template_2.html')
    documento=plantilla.render(estudiantecin_0)
    return HttpResponse(documento)"""

# def cursoFormulario(request):
#     if request.method=='POST':
#         nombre=request.POST['nombre']
#         comision=request.POST['comision']
#         curso=Curso(nombre=nombre, comision=comision)
#         curso.save()
#         return render(request, 'AppCoder/inicio.html')



#     return render(request, 'AppCoder/cursoFormulario.html')

def cursoFormulario(request):
    if request.method=='POST':
        form=CursoForm(request.POST)
        print('-------------------------------')
        print(form)
        print('-------------------------------')
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion['nombre']
            comision=informacion['comision']
            curso=Curso(nombre=nombre, comision=comision)
            curso.save()
            return render (request, 'AppCoder/inicio.html')

    else:
        formulario=CursoForm()
        return render (request, 'AppCoder/cursoFormulario.html', {'formulario':formulario})

def profeFormulario(request):
    if request.method=='POST':
        form=ProfeForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info['nombre']
            apellido=info['apellido'] 
            email=info['email']
            profe=Profesor(nombre=nombre, apellido=apellido, email=email)
            profe.save()
            return render (request, 'AppCoder/inicio.html', {"mensaje":"Profesor creado"})
    else:
        form=ProfeForm()
    return render (request, 'AppCoder/profeForm.html', {'formulario':form})

def busquedaComision(request):
    return render(request, 'AppCoder/busquedaComision.html')

def buscar(request):
    comision=request.GET['comision']
    #traeme de la base, TODOS LOS CURSOS QUE TENGAN ESA COMISION
    cursos=Curso.objects.filter(comision=comision)
    return render(request, 'AppCoder/resultadosBusqueda.html', {'cursos':cursos})



