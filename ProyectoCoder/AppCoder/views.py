
from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse
# Create your views here.


def curso(self):
    curso= Curso(nombre="Django", comision=23912)
    curso.save()
    texto= f"Curso Creado: {curso.nombre} {curso.comision}"
    return HttpResponse(texto)