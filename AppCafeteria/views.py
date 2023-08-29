from django.shortcuts import render
from django.http import HttpResponse
from .models import Cafeteria, Barista, Usuario
from .forms import CafeteriaForm, BaristaForm, UsuarioForm
# Create your views here.

def inicio(request):
    return render (request, "AppCafeteria/inicio.html")

def cafeterias(request):

    if request.method=="POST" :
        form=CafeteriaForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            direccion=info["direccion"]
            instagram=info["instagram"]
            cafeteria=Cafeteria(nombre=nombre, direccion=direccion, instagram=instagram)
            cafeteria.save()
            formulario_cafeteria=CafeteriaForm()

            return render (request, "AppCafeteria/cafeterias.html", {"mensaje": "Cafeteria Guardada", "formulario": formulario_cafeteria})
    
        else:
            return render (request, "AppCafeteria/cafeterias.html", {"mensaje": "DATOS INVALIDOS"})

    else: 
        formulario_cafeteria=CafeteriaForm()

    return render (request, "AppCafeteria/cafeterias.html", {"formulario": formulario_cafeteria})


def baristas(request):

    if request.method=="POST" :
        form=BaristaForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            cafeteria=info["cafeteria"]
            email=info["email"]
            barista=Barista(nombre=nombre, apellido=apellido, cafeteria=cafeteria, email=email)
            barista.save()
            formulario_barista=BaristaForm()

            return render (request, "AppCafeteria/baristas.html", {"mensaje": "Barista Registrado", "formulario": formulario_barista})
    
        else:
            return render (request, "AppCafeteria/baristas.html", {"mensaje": "DATOS INVALIDOS"})

    else: 
        formulario_barista=BaristaForm()

    return render (request, "AppCafeteria/baristas.html", {"formulario": formulario_barista})

def comunidad (request):
    if request.method=="POST" :
        form=UsuarioForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            usuario=Usuario(nombre=nombre, apellido=apellido, email=email)
            usuario.save()
            formulario_usuario=UsuarioForm()

            return render (request, "AppCafeteria/comunidad.html", {"mensaje": "Usuario Registrado", "formulario": formulario_usuario})
    
        else:
            return render (request, "AppCafeteria/comunidad.html", {"mensaje": "DATOS INVALIDOS"})

    else: 
        formulario_usuario=UsuarioForm()

    return render (request, "AppCafeteria/comunidad.html", {"formulario": formulario_usuario})


def busquedaCafeteria(request):
    return render(request, "AppCafeteria/busquedaCafeteria.html")
     

def buscar(request):
    nombre=request.GET["nombre"]
    if nombre != "":
        cafeterias=Cafeteria.objects.filter(nombre=nombre)
        return render(request, "AppCafeteria/resultadoBusqueda.html", {"cafeterias":cafeterias })
    else:
        return render(request, "AppCafeteria/busquedaCafeteria.html", {"mensaje": "datos incorrectos."})