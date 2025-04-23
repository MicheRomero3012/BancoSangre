from rest_framework import viewsets
from usuario.models import Usuario
from usuario.api.serializer import UsuarioSerializer
from usuario.api.permissions import IsAdminOrReadOnly  # Asegúrate de importar el permiso

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()  # Todos los usuarios
    serializer_class = UsuarioSerializer  # El serializador de los usuarios
    permission_classes = [IsAdminOrReadOnly]  # Asigna el permiso aquí para controlar el acceso
