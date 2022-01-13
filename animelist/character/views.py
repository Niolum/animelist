from rest_framework import viewsets
from .models import Character
from .serializers import CharacterListSerializer, CharacterDetailSerializer

# Create your views here.
class CharacterViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод актеров или режиссеров"""
    queryset = Character.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CharacterListSerializer
        elif self.action == "retrieve":
            return CharacterDetailSerializer