from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import *
from ckeditor.fields import RichTextField


class Sitio(models.Model):
    nombre = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=100, blank=True)
    descripcion = models.CharField(max_length=250, blank=True)
    historia = models.CharField(max_length=250, blank=True)    
    image = models.ImageField(upload_to='sitio', null=True, blank=True)
    owner = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nombre} -  {self.ciudad}'

class Restaurante(models.Model):
    nombre = models.CharField(max_length=40)
    ciudad= models.CharField(max_length=100)
    tipo_de_comida= models.CharField(max_length=100)
    experiencia = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to='restaurante', null=True, blank=True)
    owner = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nombre}  - {self.ciudad} - {self.tipo_de_comida}'

class Monumento(models.Model):
    nombre = models.CharField(max_length=40)
    ciudad= models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250, blank=True)
    historia = models.CharField(max_length=250, blank=True)  
    image = models.ImageField(upload_to='monumento', null=True, blank=True)
    owner = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.nombre} - {self.ciudad}'
		 
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatar', null=True, blank=True)

    def __str__(self):
        return f'user: {self.user.username} | url: {self.image.url}'