from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('Familiar_1/', familiar_1_html),
    path('Familiar_2/', familiar_2_html),
    path('Familiar_3/', familiar_3_hmtl),
    path('', inicio),
    path('cursos/', cursos),
    path('estudiantes/', estudiantes),
    path('profesores/', profesores),
    path('entregables/', entregables),
]
