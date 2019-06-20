from django.db import models

# Create your models here.

class Cliente(models.Model):

    nombre=models.CharField(max_length=200)
    direccion=models.CharField(max_length=250)
    MEGAS = [
        ('1M', '1M Q125'),
        ('2M', '2M Q175'),
        ('3M', '3M Q250'),
        ('4M', '4M Q315'),
    ]
    megas = models.CharField(
        max_length=2,
        choices=MEGAS,
        default='1M',
    )

    def __str__(self):
    	return '%s %s' % (self.nombre, self.megas)
