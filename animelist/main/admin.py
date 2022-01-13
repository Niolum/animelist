from django.contrib import admin
from .models import Anime, Manga, Ranobe, AnimeShots

# Register your models here.
admin.site.register(Anime)
admin.site.register(Manga)
admin.site.register(Ranobe)
admin.site.register(AnimeShots)