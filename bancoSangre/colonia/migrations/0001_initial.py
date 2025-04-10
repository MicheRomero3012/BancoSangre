# Generated by Django 5.1.7 on 2025-04-07 23:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('municipio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colonia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='municipio.municipio')),
            ],
        ),
    ]
