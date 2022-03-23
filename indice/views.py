
from string import Template
from django import template
from django.template import Context, Template, loader
from django.http import HttpResponse
import random

def inicio(request):
    return HttpResponse('Hola, soy la nueva pagina')

def otra_vista(request):
    return HttpResponse('''
                        <h1>Este es un titulo h1</h1>
                        ''')

def numero_random(request):
    numero = random.randrange(13, 180)
    texto = f'<h1>Este es tu numero random: {numero}</h1>'
    return HttpResponse(texto)

def numero_del_usuario(request, numero):
    texto = f'<h1>Este es tu numero: {numero}</h1>'
    return HttpResponse(texto)

def mi_plantilla(request):
    # plantilla = open(r'C:\Users\carmela\Desktop\mi_proyecto\mi_proyecto\mi_plantilla\mi_plantilla.html')
    #template = Template(plantilla.read())
    #context = Context(diccionario_de_datos)
    #plantilla.close()
   
    
      
    nombre = 'jorge'
    apellido = 'Atahualpa'
    
    lista = [3, 1, 2, 45, 1, 2, 3] 
        
    diccionario_de_datos = {
        'nombre': nombre,
        'apellido': apellido,
        'nombre_largo': len(nombre),
        'lista': lista 
    }
    
    template = loader.get_template('mi_plantilla.html')
    
    plantilla_preparada = template.render(diccionario_de_datos)
    
    return HttpResponse(plantilla_preparada)