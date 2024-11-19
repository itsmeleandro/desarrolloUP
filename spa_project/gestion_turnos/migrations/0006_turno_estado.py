# Generated by Django 5.1.3 on 2024-11-19 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_turnos', '0005_remove_profesional_especialidad_remove_turno_estado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='turno',
            name='estado',
            field=models.CharField(choices=[('activo', 'Activo'), ('cancelado', 'Cancelado')], default='activo', max_length=10),
        ),
    ]