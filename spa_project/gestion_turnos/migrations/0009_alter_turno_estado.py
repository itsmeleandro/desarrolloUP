# Generated by Django 5.1.3 on 2024-11-19 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_turnos', '0008_alter_turno_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turno',
            name='estado',
            field=models.CharField(choices=[('activo', 'Activo'), ('pendiente', 'Pendiente'), ('cancelado', 'Cancelado'), ('cancelado_por_cliente', 'Cancelado por Cliente'), ('cancelado_por_profesional', 'Cancelado por Profesional')], default='activo', max_length=30),
        ),
    ]