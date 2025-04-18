from django.urls import path, include
from rest_framework.routers import DefaultRouter
from donador.api.views import DonadorViewSet

router = DefaultRouter()
router.register('', DonadorViewSet, basename='donador')  # Cambié 'donadores' a ''

urlpatterns = [
    path('', include(router.urls)),  # Con esta configuración la ruta será /api/donador/
]
