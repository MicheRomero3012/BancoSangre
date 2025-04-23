from rest_framework import viewsets
from donador.models import Donador
from donador.api.serializer import DonadorSerializer
from usuario.api.permissions import IsDonadorCreateReadOnly  # Asegúrate de importar el permiso

class DonadorViewSet(viewsets.ModelViewSet):
    queryset = Donador.objects.all()  # Todos los donadores
    serializer_class = DonadorSerializer  # El serializador de los donadores
    permission_classes = [IsDonadorCreateReadOnly]  # Asigna el permiso aquí para controlar el acceso
