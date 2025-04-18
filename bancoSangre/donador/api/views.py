from rest_framework import viewsets
from donador.models import Donador
from donador.api.serializer import DonadorSerializer
from usuario.api.permissions import IsDonadorCreateReadOnly

class DonadorViewSet(viewsets.ModelViewSet):
    queryset = Donador.objects.all()
    serializer_class = DonadorSerializer
    permission_classes = [IsDonadorCreateReadOnly]