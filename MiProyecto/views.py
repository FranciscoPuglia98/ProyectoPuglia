
from asyncio.base_events import _Context
from decimal import Context
from string import Template
from django.http import HttpResponse
import random

def inicio(request):
    return HttpResponse('Hola, soy la nueva pagina')

def otra_vista(request):
    return HttpResponse('''
                         <h1>Puto el que lee</h1>
                        ''')


def numero_random(request):
    numero= random.randrange(15, 180)
    return HttpResponse(numero)


def numero_del_usuario(request, numero):
    texto= f'<h1>Este es tu numero: {numero}</h1>'
    return HttpResponse(texto)


def mi_plantilla(request):
    plantilla = open(r"C:\Users\Usuario\Desktop\MiProyecto\MiProyecto\plantillas\mi_plantilla.html")

    template = Template(plantilla.read())

    context = Context()

    plantilla_preparada = template.render(context)

    return HttpResponse(plantilla_preparada)