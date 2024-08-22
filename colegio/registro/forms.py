from django import forms
from .models import Docente, Estudiante, Curso

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['nombre', 'apellido', 'email', 'telefono', 'direccion']

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'fecha_nacimiento']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'codigo']