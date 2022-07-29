# Generated by Django 4.0.6 on 2022-07-29 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
        ('usuarios', '0001_initial'),
        ('horarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='puntosdeacceso',
            name='horarios_de_acceso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='puntos_de_acceso', to='horarios.horario'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='usuario_admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empresa_admin', to='usuarios.usuario'),
        ),
    ]