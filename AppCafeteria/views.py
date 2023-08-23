from django.shortcuts import render
from django.http import HttpResponse
from .models import Cafeteria, Barista, Usuario
# Create your views here.

def crear_cafeteria(request):

    nombre_cafeteria= "Intimo Café"
    direccion_cafeteria= "la rioja 151"
    instagram_cafeteria= "@intimocafeteria"
    print(" Creando Cafeteria ")
    cafeteria=Cafeteria(nombre=nombre_cafeteria, direccion=direccion_cafeteria, instagram=instagram_cafeteria)
    cafeteria.save()
    respuesta=f"Se creo la cafeteria: {nombre_cafeteria} ---> {instagram_cafeteria}"

    return HttpResponse(respuesta)

def listar_cafeterias(request):
    cafeterias=Cafeteria.objects.all()
    respuesta=""
    for cafeteria in cafeterias:
        respuesta+=f"{cafeteria.nombre} - {cafeteria.instagram}"
    return HttpResponse(respuesta) 
