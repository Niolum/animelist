from rest_framework import viewsets
from .serializers import CommentCreateSerializer

# Create your views here.
class CommentCreateViewSet(viewsets.ModelViewSet):
    serializer_class = CommentCreateSerializer