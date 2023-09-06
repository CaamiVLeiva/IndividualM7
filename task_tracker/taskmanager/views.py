from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, CustomAuthenticationForm, TaskForm, TaskFilterForm
from .models import Task,Observacion, Prioridad

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
    tareas_pendientes = Task.objects.filter(usuario=request.user).order_by('fecha_vencimiento').prefetch_related('etiquetas')  # Usamos prefetch_related para cargar las etiquetas relacionadas
    if request.method == 'GET':
        form = TaskFilterForm(request.GET)
        if form.is_valid():
            estado = form.cleaned_data.get('estado')
            etiquetas = form.cleaned_data.get('etiquetas')
            fecha_vencimiento = form.cleaned_data.get('fecha_vencimiento')
            if estado:
                tareas_pendientes = tareas_pendientes.filter(estado=estado)
            if etiquetas:
                tareas_pendientes = tareas_pendientes.filter(etiquetas__in=etiquetas)
            if fecha_vencimiento:
                tareas_pendientes = tareas_pendientes.filter(fecha_vencimiento__date=fecha_vencimiento)
            
            if 'limpiar_filtros' in request.GET:
                return redirect('listar_tareas_pendientes')
    else:
        form = TaskFilterForm()
    return render(request, 'taskmanager/listar_tareas_pendientes.html', {'form': form, 'tareas_pendientes': tareas_pendientes})

@login_required
def crear_tarea(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.asignado_a = form.cleaned_data['asignado_a']

            tarea.prioridad = form.cleaned_data['prioridad']
            
            tarea.usuario = request.user
            tarea.save()
            form.save_m2m()
            return redirect('listar_tareas_pendientes')
    else:
        form = TaskForm()
    return render(request, 'taskmanager/crear_tarea.html', {'form': form})


@login_required
def ver_tarea(request, task_id):
    tarea = get_object_or_404(Task, pk=task_id)
    etiquetas = tarea.etiquetas.all()
    prioridad = tarea.prioridad

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'completar':
            tarea.estado = 'completada'
            tarea.save()
        elif action == 'eliminar':
            tarea.delete()
        elif action == 'guardar_observaciones':
            observaciones = request.POST.get('observaciones')
            Observacion.objects.create(tarea=tarea, texto=observaciones)
            # Redirige a la vista de visualización de tareas después de guardar observaciones
            return redirect('ver_tarea', task_id=task_id)

    tareas_ordenadas = Task.objects.filter(usuario=request.user).order_by('fecha_vencimiento').prefetch_related('etiquetas')
    observaciones_tarea = Observacion.objects.filter(tarea=tarea).order_by('-fecha_creacion')
    # Pasa las etiquetas y observaciones a la plantilla
    return render(request, 'taskmanager/ver_tarea.html', {'task': tarea, 'etiquetas': etiquetas, 'tareas_ordenadas': tareas_ordenadas, 'observaciones_tarea': observaciones_tarea, 'prioridad': prioridad})



@login_required
def editar_tarea(request, task_id):
    tarea = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect('ver_tarea', task_id=task_id)
    else:
        form = TaskForm(instance=tarea)
    return render(request, 'taskmanager/editar_tarea.html', {'form': form, 'task': tarea})


def eliminar_tarea(request, task_id):
    tarea = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        tarea.delete()
        return redirect('listar_tareas_pendientes')
    return render(request, 'taskmanager/listar_tareas_pendientes', {'task': tarea})

def editar_observaciones(request, task_id):
    tarea = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        observaciones = request.POST.get('observaciones')
        tarea.observaciones = observaciones
        tarea.save()
        return redirect('ver_tarea', task_id=task_id)
    return render(request, 'taskmanager/editar_observaciones.html', {'task': tarea})