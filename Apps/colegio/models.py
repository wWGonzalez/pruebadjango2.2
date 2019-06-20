from django.db import models
import datetime
# Create your models here.



class Estudiante(models.Model):
	carnet=models.CharField(max_length=200)
	nombre=models.CharField(max_length=200)
	fecha_de_nacimiento=models.DateField(("Date"), default=datetime.date.today)
	def __str__(self):
		return self.nombre

class Curso(models.Model):
	codigo=models.CharField(max_length=200)
	nombre=models.CharField(max_length=200)
	def __str__(self):
		return '%s %s' % (self.codigo, self.nombre)

class Grado(models.Model):
	nombre=models.CharField(max_length=200)
	def __str__(self):
		return self.nombre


class Asignacion(models.Model):
	estudiante=models.ForeignKey(Estudiante, on_delete=models.CASCADE)
	curso=models.ForeignKey(Curso, on_delete=models.CASCADE)
	grado=models.ForeignKey(Grado, on_delete=models.CASCADE)
	def __str__ (self):
		return self.estudiante

