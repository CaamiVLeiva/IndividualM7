from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Task, Tag


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
    etiquetas = forms.ModelChoiceField(
        queryset=Tag.objects.all(),
        empty_label="Selecciona una etiqueta",  # Texto para la opción vacía
        required=False,  # Para permitir que el usuario no seleccione ninguna etiqueta
    )
    class Meta:
        model = Task
        fields = ['titulo','descripcion','fecha_vencimiento','etiquetas']
    widgets = {
        'fecha_vencimiento': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    }
    
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['fecha_vencimiento'].widget.attrs.update({'class': 'datepicker'})