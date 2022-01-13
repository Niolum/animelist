from rest_framework import viewsets
from .models import Author
from .serializers import AuthorListSerializer, AuthorDetailSerializer

# Create your views here.
class AuthorsViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод актеров или режиссеров"""
    queryset = Author.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return AuthorListSerializer
        elif self.action == "retrieve":
            return AuthorDetailSerializer