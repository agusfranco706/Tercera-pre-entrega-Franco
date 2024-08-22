from django.shortcuts import render, redirect
from .forms import DocenteForm, EstudianteForm, CursoForm
from .models import Docente, Estudiante, Curso

def alta_docente(request):
    if request.method == 'POST':
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            return
        redirect('lista_docentes')
    else:
        form = DocenteForm()
        return render(request, 'registro/alta_docente.html', {'form': form})
    
def buscar_docente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        docentes = Docente.objects.filter(nombre__icontains=nombre)
        return render(request, 'registro/buscar_docente.html', {'docentes': docentes})
    return render(request, 'registro/buscar_docente.html')

def lista_docentes(request):
    docentes = Docente.objects.all()
    return render(request, 'registro/lista_docentes.html', {'docentes': docentes})



