from django.db import models
from django.utils import timezone
from Asignaturas.models import Asignatura


class Estudiante(models.Model):
    nombre = models.CharField('Nombre Estudiante', max_length=150)
    apellidos = models.CharField('Apellidos Estudiante', max_length=200)
    documento = models.IntegerField(blank=False, null=True, verbose_name='Documento')
    telefono = models.IntegerField(blank=False, null=True, verbose_name='Celular')
    email = models.EmailField('Email', max_length=120, blank=False, null=False)
    estado = models.BooleanField('Activo/Inactivo', default=False)

    timestamp = models.DateTimeField('Fecha registro', default=timezone.now)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.PROTECT)

    def __str__(self):
        return '{0},{1}'.format(self.apellidos, self.nombre)
