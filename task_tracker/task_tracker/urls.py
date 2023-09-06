"""
URL configuration for task_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from taskmanager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('taskmanager.urls')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('create_user/', views.create_user, name= 'create_user'),
    path('crear_tarea', views.crear_tarea, name='crear_tarea'),
    path('ver_tarea/<int:task_id>', views.ver_tarea, name='ver_tarea'),
    path('tareas_pendientes/', views.listar_tareas_pendientes, name='listar_tareas_pendientes'),
    path('editar_tarea/<int:task_id>/', views.editar_tarea, name='editar_tarea'),
    path('eliminar_tarea/<int:task_id>/', views.eliminar_tarea, name='eliminar_tarea'),
    path('editar_observaciones/<int:task_id>/', views.editar_observaciones, name='editar_observaciones'),
    path('', views.index, name='index'),
]
