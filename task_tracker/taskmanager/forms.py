from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Task, Tag, Prioridad

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'password1', 'password2']

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        label="Nombre de Usuario",  # Personaliza la etiqueta del campo de usuario
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(
        label="Contraseña",  # Personaliza la etiqueta del campo de contraseña
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
        error_messages={
            'invalid_login': 'Por favor, ingrese un nombre de usuario y contraseña válidos. Tenga en cuenta que ambos campos son sensibles a mayúsculas y minúsculas.',
            }
    )

class TaskForm(forms.ModelForm):
    etiquetas = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    # Agrega un campo para seleccionar la prioridad
    prioridad = forms.ModelChoiceField(
        queryset=Prioridad.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False,
    )

    class Meta:
        model = Task
        fields = ['titulo', 'descripcion', 'fecha_vencimiento', 'asignado_a', 'etiquetas', 'prioridad']

    widgets = {
        'fecha_vencimiento': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['fecha_vencimiento'].widget.attrs.update({'class': 'datepicker'})

class TaskFilterForm(forms.Form):
    ESTADO_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
    )
    estado = forms.ChoiceField(choices=Task.ESTADO_CHOICES, required=False)
    etiquetas = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    fecha_vencimiento = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

class TaskEditForm(forms.ModelForm):
    prioridad = forms.ModelChoiceField(
        queryset=Prioridad.objects.all(),
        required=False,
    )

    class Meta:
        model = Task
        fields = ['titulo', 'descripcion', 'fecha_vencimiento', 'etiquetas', 'prioridad']

    widgets = {
        'fecha_vencimiento': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    }

    def __init__(self, *args, **kwargs):
        super(TaskEditForm, self).__init__(*args, **kwargs)
        self.fields['fecha_vencimiento'].widget.attrs.update({'class': 'datepicker'})
