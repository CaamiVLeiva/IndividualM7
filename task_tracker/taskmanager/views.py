from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, CustomAuthenticationForm, TaskForm
from .models import Task

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Autenticar al usuario
            login(request, form.get_user())
            return redirect('listar_tareas_pendientes')  
    else:
        form = CustomAuthenticationForm()
    return render(request, 'taskmanager/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')  # Redirige al inicio de sesión.


def index(request):
    return render(request, 'taskmanager/index.html')

def create_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente después de crear el usuario
            return redirect('listar_tareas_pendientes')  # Redirige a la página de inicio
    else:
        form = CustomUserCreationForm()
    return render(request, 'taskmanager/create_user.html', {'form': form})

@login_required
def listar_tareas_pendientes(request):
    tareas_pendientes = Task.objects.filter(estado='pendiente', usuario=request.user).order_by('fecha_vencimiento')
    return render(request, 'taskmanager/listar_tareas_pendientes.html', {'tareas_pendientes': tareas_pendientes})

def crear_tarea(request):
    if request.method == 'POST':
        # Procesar el formulario de creación de tarea
        form = TaskForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.usuario = request.user
            tarea.save()
            return redirect('listar_tareas_pendientes')  # Redirigir a la lista de tareas pendientes
    else:
        form = TaskForm()  # Mostrar un formulario en blanco

    return render(request, 'taskmanager/crear_tarea.html', {'form': form})

def ver_tarea(request, task_id):
    tarea = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'completar':
            tarea.estado = 'completada'
            tarea.save()
    return render(request, 'taskmanager/ver_tarea.html', {'task': tarea})

def editar_tarea(request, task_id):
    tarea = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('listar_tareas_pendientes')
    else:
        form = TaskForm(instance=tarea)
    return render(request, 'taskmanager/editar_tarea.html', {'form': form, 'task': tarea})

def eliminar_tarea(request, task_id):
    tarea = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        tarea.delete()
        return redirect('listar_tareas_pendientes')
    return render(request, 'taskmanager/listar_tareas_pendientes', {'task': tarea})
