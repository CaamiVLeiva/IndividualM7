from django.contrib import admin
from .models import Tag, Task
# Register your models here.
@admin.register(Tag)
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(Task)