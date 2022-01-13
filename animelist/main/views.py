from django.db import models
from rest_framework import viewsets
from .serializers import (AnimeListSerializer, 
    AnimeDetailSerializer,
    MangaListSerializer,   
    MangaDetailSerializer, 
    RanobeListSerializer, 
    RanobeDetailSerializer
)
from .models import Anime, Manga, Ranobe
from rating.service import get_ip_client

# Create your views here.
class AnimeViewSet(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        animes = Anime.objects.filter(draft=False).annotate(
            rating_user=models.Count('ratings', filter=models.Q(ratings__ip=get_ip_client(self.request)))
        ).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
        )
        return animes

    def get_serializer_class(self):
        if self.action == 'list':
            return AnimeListSerializer
        elif self.action == "retrieve":
            return AnimeDetailSerializer


class MangaViewSet(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        mangas = Manga.objects.filter(draft=False).annotate(
            rating_user=models.Count('ratings', filter=models.Q(ratings__ip=get_ip_client(self.request)))
        ).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
        )
        return mangas
    
    def get_serializer_class(self):
        if self.action == 'list':
            return MangaListSerializer
        elif self.action == "retrieve":
            return MangaDetailSerializer


class RanobeViewSet(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        ranobes = Ranobe.objects.filter(draft=False).annotate(
            rating_user=models.Count('ratings', filter=models.Q(ratings__ip=get_ip_client(self.request)))
        ).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
        )
        return ranobes

    def get_serializer_class(self):
        if self.action == 'list':
            return RanobeListSerializer
        elif self.action == "retrieve":
            return RanobeDetailSerializer