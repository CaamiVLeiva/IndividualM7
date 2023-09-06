# Generated by Django 4.2.5 on 2023-09-06 06:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taskmanager', '0004_observacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='asignado_a',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tareas_asignadas', to=settings.AUTH_USER_MODEL),
        ),
    ]
