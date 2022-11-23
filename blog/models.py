from django.db import models
from django.contrib.auth.models import User

class Sitio(models.Model):
    nombre = models.CharField(max_length=40)
    ciudad= models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.nombre} -  {self.ciudad}'

class Restaurante(models.Model):
    nombre = models.CharField(max_length=40)
    ciudad= models.CharField(max_length=100)
    tipo_de_comida= models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre}  - {self.ciudad} - {self.tipo_de_comida}'

class Monumento(models.Model):
    nombre = models.CharField(max_length=40)
    ciudad= models.CharField(max_length=100)
    fecha= models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.ciudad} - Fecha: {self.fecha}'
		 
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars', null=True, blank=True)

    def __str__(self):
        return f'url: {self.image.url}'