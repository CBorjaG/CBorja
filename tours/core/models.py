
from django.db import models
import uuid 


# Create your models here.


class Destino(models.Model):
	nombre = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=20)

	def __str__(self):
		return self.nombre

class Transporte(models.Model):
	nombre = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=20)
	
	def __str__(self):
		return self.nombre

class Nacionalidad(models.Model):
	nombre = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=20)

	def __str__(self):
		return self.nombre
	class Meta:
		verbose_name = 'Nacionalidades'
		verbose_name_plural = 'Nacionalidad'	

class Cliente(models.Model):
	"""docstring for ClassName"""
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID Unica')
	nombre = models.CharField(max_length=200, blank=True, help_text='Ingrese Nombre cliente')
	apellido = models.CharField(max_length=200, blank=True, help_text='Ingrese Apellido cliente')
	email = models.EmailField('Email', max_length=50, blank=True, help_text='Ingrese Correo cliente') 
	inicio = models.DateField(help_text='Ingrese Fecha Inicio viaje')
	fin = models.DateField(help_text='Ingrese Fecha Termino viaje')
	destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
	transporte = models.ForeignKey(Transporte, on_delete=models.CASCADE)
	nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE)
	
	def str(self):
		return self.id

	def __str__(self):
		return self.nombre
	class Meta:
		verbose_name = 'Clientes'
		verbose_name_plural = 'Cliente'	
    
	

