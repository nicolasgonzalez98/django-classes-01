from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index ( request ):
    return HttpResponse( "¡Hola, mundo!" )

def alumnos(request):
    return HttpResponse('Alumnos')

def acerca_de ( request ):
    return HttpResponse( "¡Curso de Python y Django!" )