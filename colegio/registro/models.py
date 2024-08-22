from django.db import models

class Docente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.nombre
    
    