from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomAuthenticationForm

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Autenticar al usuario
            login(request, form.get_user())
            return redirect('landing')  
    else:
        form = CustomAuthenticationForm()
    return render(request, 'taskmanager/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')  # Redirige al inicio de sesión.


def index(request):
    return render(request, 'taskmanager/index.html')


def landing(request):
    return render(request, 'taskmanager/landing.html')


def create_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión automáticamente después de crear el usuario
            return redirect('landing')  # Redirige a la página de inicio
    else:
        form = CustomUserCreationForm()
    return render(request, 'taskmanager/create_user.html', {'form': form})

