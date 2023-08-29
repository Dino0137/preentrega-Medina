from django import forms

class CafeteriaForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    direccion=forms.CharField(max_length=50)
    instagram=forms.CharField(max_length=50)


class BaristaForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    cafeteria=forms.CharField(max_length=50)
    email=forms.EmailField()

class UsuarioForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()