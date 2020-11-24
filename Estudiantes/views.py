from django.shortcuts import render
from django.views.generic import ListView
from .models import Estudiante

class ListStudent(ListView):
   model = Estudiante
   template_name = 'students/listar.html'
   contex_object_name = "list_student"
   queryset = Estudiante.objects.all()