# Generated by Django 5.1.7 on 2025-04-08 17:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('direccion', '0001_initial'),
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidoP', models.CharField(max_length=100)),
                ('apellidoM', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('primeraDonacion', models.DateField()),
                ('ultimaDonacion', models.DateField()),
                ('tipoSangre', models.CharField(max_length=5)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=5)),
                ('estado', models.BooleanField()),
                ('telefonoUno', models.CharField(max_length=15)),
                ('telefonoDos', models.CharField(blank=True, max_length=15, null=True)),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='direccion.direccion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.usuario')),
            ],
        ),
    ]
