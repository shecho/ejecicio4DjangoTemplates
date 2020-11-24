from django.urls import path
from .views import ListAsignatura

urlpatterns = [
    path('', ListAsignatura.as_view(), name='list_asignatura')
]
