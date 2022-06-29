from django.http import HttpResponse
import datetime
from django.template import Context, Template

def saludo(request):
    return HttpResponse("hola mundo asdasdasd!!!!")


def segunda_vista(request):
    return HttpResponse ("Segunda prueba en urls")


def dia_de_hoy(request):
    dia=datetime.datetime.today()
    codigohtml="<h1>Hoy es : "+str(dia)+"</h1>"
    return HttpResponse(codigohtml)

def saludo_con_nombre(self, nombre):
    return HttpResponse("<h1>Hola mi nombre es: "+nombre+"</h1>")

def calcula_Año_Nacimiento(self, edad):
    return HttpResponse("<h1>Tu año de nacimiento es: "+str(int(datetime.datetime.now().year)-int(edad))+"</h1>")


def probandohtml(self):
    miarchivo=open("C:/Users/ftarela/Desktop/Visual Coderhouse/Proyecto1/Template/template1.html")
   
    plantilla=Template(miarchivo.read())
    miarchivo.close
    contexto=Context()

    documento=plantilla.render(contexto)

    return HttpResponse(documento)
