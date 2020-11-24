from django.views.generic import ListView
from .models import Asignatura

class ListAsignatura(ListView):
   model = Asignatura
   template_name = 'asignaturas/listado.html'