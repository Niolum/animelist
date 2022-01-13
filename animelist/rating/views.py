from .serializers import CreateRatingSerializer
from rest_framework import viewsets
from .service import get_ip_client

# Create your views here.
class AddStarRatingViewSet(viewsets.ModelViewSet):
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save(ip=get_ip_client(self.request))