import datetime
from django import forms
from django.forms import ModelForm
from blog.models import Restaurante, Sitio, Monumento

class SitioForm(forms.Form):
    nombre = forms.CharField(max_length=40, label='Nombre')
    ciudad= forms.CharField(max_length=100, label='Ciudad')
    
class RestauranteForm(forms.Form):
    nombre = forms.CharField(max_length=40, label='Nombre')
    ciudad= forms.CharField(max_length=100, label='Ciudad')
    tipo_de_comida= forms.CharField(max_length=100, label='Tipo de comida')

class MonumentoForm(forms.Form):
    nombre = forms.CharField(max_length=40, label='Nombre')
    ciudad= forms.CharField(max_length=100, label='Ciudad')
    fecha= forms.IntegerField( label='Fecha')