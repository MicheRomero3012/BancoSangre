from rest_framework import viewsets
from usuario.models import Usuario
from usuario.api.serializer import UsuarioSerializer
from usuario.api.permissions import IsAdminOrReadOnly  # Asegúrate de importar el permiso

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAdminOrReadOnly]  # Asigna el permiso aquí
