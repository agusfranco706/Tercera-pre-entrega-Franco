from django.urls import path 
from . import views 

urlpatterns = [
path('alta_docente/', views.alta_docente, name='alta_docente'),
path('buscar_docente/', views.buscar_docente, name='buscar_docente'),
path('lista_docentes/', views.lista_docentes, name='lista_docentes'),
]