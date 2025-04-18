# script_roles.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bancoSangre.settings')
django.setup()

from bancoSangre.rol.models import Rol

roles_defecto = ["donador", "administrador"]

for nombre in roles_defecto:
    rol, creado = Rol.objects.get_or_create(nombre=nombre)
    if creado:
        print(f'✅ Rol "{nombre}" creado.')
    else:
        print(f'ℹ️ Rol "{nombre}" ya existe.')
