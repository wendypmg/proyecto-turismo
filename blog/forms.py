from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget
from blog.models import *

#TURISMO
class SitioForm(forms.Form):
    nombre = forms.CharField(max_length=40, label='Nombre')
    ciudad = forms.CharField(max_length=100, label='Ciudad')
    descripcion = forms.CharField(max_length=250, label='Descripción')
    historia = forms.CharField(max_length=250, label='Historia')
    image = forms.ImageField()

    class Meta:
        model = Sitio
        fields = ['nombre', 'ciudad', 'descripcion', 'historia', 'image']
    
class RestauranteForm(forms.Form):
    nombre = forms.CharField(max_length=40, label='Nombre')
    ciudad = forms.CharField(max_length=100, label='Ciudad')
    tipo_de_comida = forms.CharField(max_length=100, label='Tipo de comida')
    experiencia = forms.CharField(max_length=250, label='Opinión')
    image = forms.ImageField()

    class Meta:
        model = Restaurante
        fields = ['nombre', 'ciudad', 'tipo_de_comida', 'experiencia', 'image']
    

class MonumentoForm(forms.Form):
    nombre = forms.CharField(max_length=40, label='Nombre')
    ciudad= forms.CharField(max_length=100, label='Ciudad')
    descripcion = forms.CharField(max_length=250, label='Descripción')
    historia = forms.CharField(max_length=250, label='Historia')
    image = forms.ImageField()

    class Meta:
        model = Monumento
        fields = ['nombre', 'ciudad', 'descripcion', 'historia', 'image']


#USUARIO
class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label='Username', min_length=3)
    first_name = forms.CharField(label='Nombre', min_length=3)
    last_name = forms.CharField(label='Apellido', min_length=3)
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        ]


class UserEditForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        widgets = {
            'email': forms.TextInput(attrs={'readonly': 'readonly'}),
        }


class AvatarForm(ModelForm):
    class Meta:
        model = Avatar
        fields = ('image', )