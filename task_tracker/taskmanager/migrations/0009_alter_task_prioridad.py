# Generated by Django 4.2.5 on 2023-09-06 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0008_alter_task_prioridad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='prioridad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='taskmanager.prioridad'),
        ),
    ]
