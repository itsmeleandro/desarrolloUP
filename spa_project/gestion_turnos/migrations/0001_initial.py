# Generated by Django 5.1.3 on 2024-11-19 05:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidad', models.CharField(max_length=100)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dias_disponibles', models.CharField(help_text='Días de la semana disponibles (ejemplo: Lunes, Martes)', max_length=100)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('profesional', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='agenda', to='gestion_turnos.profesional')),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField()),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('cancelado', 'Cancelado'), ('realizado', 'Realizado')], default='pendiente', max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turnos', to=settings.AUTH_USER_MODEL)),
                ('profesional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turnos', to='gestion_turnos.profesional')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_turnos.servicio')),
            ],
        ),
    ]
