from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('Familiar_1/', familiar_1_html),
    path('Familiar_2/', familiar_2_html),
    path('Familiar_3/', familiar_3_hmtl),
    path('', inicio, name='inicio'),
    path('cursos/', cursos, name='cursos'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('profesores/', profesores, name='profesores'),
    path('entregables/', entregables, name='entregables'),
    path('estudiantecito/', estudiantecito, name='estudiantecito'),
    path('cursoFormulario/', cursoFormulario, name='cursoFormulario'),
    path('profeFormulario/', profeFormulario, name='profeFormulario'),
    path('busquedaComision/', busquedaComision, name='busquedaComision'),
    path('buscar/', buscar, name='buscar'),
]
