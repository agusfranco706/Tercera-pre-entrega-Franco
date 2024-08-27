from django.contrib import admin

from .models import Docente, Curso, Clase

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono', 'direccion')
    search_fields = ('nombre', 'apellido', 'email')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'curso')
    search_fields = ('nombre',)
    list_filter = ('curso',)
# Register your models here.
