from django.db import models

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
		
		  
