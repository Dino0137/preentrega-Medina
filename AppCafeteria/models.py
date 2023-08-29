from django.db import models

# Create your models here.
class Cafeteria(models.Model):
    nombre=models.CharField(max_length=50 , unique=True)
    direccion=models.CharField(max_length=50)
    instagram=models.CharField(max_length=50)
    def __str__ (self):
        return f"{self.nombre} - {self.instagram} " 

class Barista(models.Model):
    nombre=models.CharField(max_length=50 , unique=True)
    apellido=models.CharField(max_length=50)
    cafeteria=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    def __str__ (self):
        return f"{self.nombre} - {self.apellido} "

class Usuario(models.Model):
    nombre=models.CharField(max_length=50 , unique=True)
    apellido=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    def __str__ (self):
        return f"{self.nombre} - {self.apellido} "

