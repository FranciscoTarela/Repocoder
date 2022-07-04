from django.shortcuts import render
from Familia_APP.models import Familiar
from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime
# Create your views here.


def familiares(request):
    familiares = Familiar(nombre='Francisco ', apellido='Tarela ', dni=37432672 , fecha="1993-04-23")
    texto=f"<br>Familiar Agregado {familiares.nombre}{familiares.apellido}DNI {familiares.dni} Nacimiento {familiares.fecha}</br>\n"
    familiares = Familiar(nombre='Carlos ',apellido='Tarela ',dni=8462154 , fecha="1950-8-30")
    texto+=f"<br>Familiar Agregado {familiares.nombre}{familiares.apellido} DNI {familiares.dni} Nacimiento {familiares.fecha}</br>\n"
    familiares = Familiar(nombre=' Marcela ',apellido='Galante ',dni=10180457, fecha="1960-9-19")
    texto+=f"<br>Familiar Agregado {familiares.nombre}{familiares.apellido} DNI {familiares.dni} Nacimiento {familiares.fecha}</br>\n"
    familiares.save()


    html= open("C:/Users/ftarela/Desktop/Visual Coderhouse/Proyecto_Familiar/Familia_APP/templates/template.html")

    plantilla= Template(html.read())

    html.close()

    micontexto = Context(familiares)

    texto+=plantilla.render (micontexto)

    return HttpResponse (texto)