import datetime
from django import forms
from django.forms import ModelForm
from blog.models import Restaurante, Sitio, Monumento
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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

'''class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}
'''