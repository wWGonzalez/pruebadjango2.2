from django.contrib import admin
from .models import Estudiante,Curso,Grado,Asignacion

# Register your models here.

admin.site.register(Estudiante)
admin.site.register(Curso)
admin.site.register(Grado)
admin.site.register(Asignacion)