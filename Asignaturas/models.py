from django.db import models
from django.utils import timezone


class Asignatura(models.Model):
    nombre= models.CharField('Nombre Clase', max_length=80)
    codigo = models.CharField('Codigo Clase', max_length=80)
    estado = models.BooleanField('Activo/Inactivo', default=False)
    timestamp = models.DateTimeField('Fecha registro', default=timezone.now)

    def __str__(self):
        return self.nombre
