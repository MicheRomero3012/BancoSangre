# 🩸 Manual de Instalación y Configuración del Proyecto BancoSangre

---

## 1. Clonación del Repositorio con Todas las Ramas

### Clonar el repositorio con todas sus ramas remotas

```bash
git clone --branch main https://github.com/MicheRomero3012/BancoSangre.git

    Esto descarga el repositorio y te coloca directamente en la rama main.

Verificar las ramas disponibles

git branch -a

    Muestra las ramas locales y remotas (remotes/origin/...).

Cambiar a otra rama

git checkout frontend

    Cambia tu rama activa a frontend.

Actualizar las ramas remotas

git fetch

    Obtiene las últimas actualizaciones del repositorio remoto.

2. Creación del Entorno Virtual
En Windows

python -m venv venv
venv\Scripts\activate

En Ubuntu

python3 -m venv venv
source venv/bin/activate

Instalar las dependencias

pip install -r requirements.txt

3. Instalación de PostgreSQL y psycopg2

pip install psycopg2

4. Configuración de la Base de Datos bancodb en PostgreSQL
Desde SQL Shell (psql):

    Server: localhost

    Username: postgres

    Password: (tu contraseña)

CREATE DATABASE bancodb;
\c bancodb
\dt

5. Configuración del Proyecto en Django

En bancoSangre/settings.py, configura la conexión a PostgreSQL:

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'bancodb',
       'USER': 'postgres',
       'PASSWORD': '689447',
       'HOST': 'localhost',
       'PORT': '5432',
   }
}

6. Aplicar Migraciones y Crear Roles por Defecto
Crear y aplicar migraciones

python manage.py makemigrations
python manage.py migrate

Ejecutar el script que crea los roles por defecto

python script_roles.py

    Este script crea los roles "administrador" y "donador" automáticamente.
    Si ya existen, no los duplicará.

7. Creación del Superusuario Administrador

Para poder generar tokens y realizar acciones administrativas, sigue estos pasos:
Crear el Superusuario Administrador desde el Shell de Django

    Abre el shell de Django:

python manage.py shell

Dentro del shell, ejecuta el siguiente código para crear un superusuario administrador, asignarle el rol de administrador y generar el token de acceso para la API:

from usuario.models import Usuario
from rol.models import Rol
from rest_framework.authtoken.models import Token

# Crear o obtener el rol de administrador
rol_admin, creado = Rol.objects.get_or_create(nombre="Administrador")

# Crear el superusuario (ajusta nombre, correo y contraseña)
superusuario = Usuario.objects.create(
    nombre_usuario="admin",
    correo="admin@example.com",
    contraseña="admin123",  # Tu modelo se encargará de encriptarla automáticamente
    sexo="M",
    rol=rol_admin
)

# Generar el token para el superusuario
token, creado = Token.objects.get_or_create(user=superusuario)

# Mostrar el token generado
print(f"✅ Superusuario creado con token:\n🔑 {token.key}")

Esto creará un usuario con el nombre admin, el correo admin@example.com y la contraseña admin123. Recuerda ajustar estos valores según tus necesidades.

Al finalizar, el sistema generará un token que se mostrará en la terminal, el cual puedes usar para autenticarte en la API con Postman o cualquier otra herramienta.

Para salir del shell, simplemente ejecuta:

    exit()

Con esto, ya tendrás un superusuario administrador creado con el rol adecuado y listo para acceder a las funcionalidades administrativas de la API, además de contar con un token de autenticación.

8. Ejecutar el Proyecto

python manage.py runserver

    El proyecto estará disponible en:
    http://127.0.0.1:8000/

9. Pruebas de la API

Accede con tu navegador o Postman a:

    Usuarios:
    http://127.0.0.1:8000/api/usuarios/

    Donadores:
    http://127.0.0.1:8000/api/donadores/

    Los permisos funcionan de la siguiente forma:

        Donadores: Solo pueden ver y registrar datos (GET y POST).

        Administradores: Pueden ver, crear, editar y eliminar.

10. Verificar Roles y Permisos

En el admin de Django (/admin):

    Asegúrate de que los usuarios tienen asignado el rol adecuado (donador o administrador).

    Verifica que los permisos estén funcionando según el tipo de rol.

11. Comandos útiles
Salir del shell de Django

exit()

O Ctrl + D (Linux/Mac) | Ctrl + Z + Enter (Windows)

    📌 Manual de instalación y configuración del Proyecto BancoSangre.
    Desarrollado por el equipo 3 — @michee 💻❤️