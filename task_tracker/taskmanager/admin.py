from django.contrib import admin
from .models import Tag, Task, Prioridad
# Register your models here.
@admin.register(Tag)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(Task)
admin.site.register(Prioridad)