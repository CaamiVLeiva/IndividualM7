from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Tag(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Prioridad(models.Model):
    nombre = models.CharField(max_length=50)
    prioridad = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Task(models.Model):
    ESTADO_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
    )

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_vencimiento = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    etiquetas = models.ManyToManyField(Tag, related_name='tareas')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    observaciones = models.TextField(blank=True, null=True)
    asignado_a = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tareas_asignadas', blank=True, null=True)
    prioridad = models.ForeignKey('Prioridad', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.titulo
    
class Observacion(models.Model):
    tarea = models.ForeignKey(Task, related_name='observaciones_task', on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

