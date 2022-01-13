from django.db import models
from genre.models import Genre
from author.models import Author
from character.models import Character
from publisher.models import Studio, Publisher

# Create your models here.
class General(models.Model):
    STATUS_ANNOUNCED = 'announenced'
    STATUS_PUBLISHED_NOW = 'published now'
    STATUS_PUBLISHED_ALREADY = 'published already'
    STATUS_SUSPENDED = 'suspended'
    STATUS_DISCONTINUED = 'discontinued'

    STATUS_CHOICES = (
        (STATUS_ANNOUNCED, 'Анонсировано'),
        (STATUS_PUBLISHED_NOW, 'Сейчас выходит'),
        (STATUS_PUBLISHED_ALREADY, 'Вышло'),
        (STATUS_SUSPENDED, 'Приостановлено'),
        (STATUS_DISCONTINUED, 'Прекращено')
    )
    
    title = models.CharField(max_length=100, verbose_name='Название')
    status = models.CharField(max_length=100, verbose_name='Статус', choices=STATUS_CHOICES, blank=True)
    poster = models.ImageField(verbose_name='Постер', upload_to='main/', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    license = models.CharField(max_length=100, verbose_name='Лицензировано', blank=True)
    slug = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField(verbose_name='Черновик', default=False)
    genres = models.ManyToManyField(Genre, verbose_name='Жанры')
    authors = models.ManyToManyField(Author, verbose_name='Авторы', blank=True)
    characters = models.ManyToManyField(Character, verbose_name='Персонажи', blank=True)

    def __str__(self):
        return self.title


class Anime(General):
    STATUS_TV_SERIAS = 'TV serias'
    STATUS_FILM = 'film'
    STATUS_OVA = 'OVA'
    STATUS_ONA = 'ONA'
    STATUS_SPECIAL = 'special'

    STATUS_CHOICES_TYPES = (
        (STATUS_TV_SERIAS, 'ТВ сериал'),
        (STATUS_FILM, 'Фильм'),
        (STATUS_OVA, 'OVA'),
        (STATUS_ONA, 'ONA'),
        (STATUS_SPECIAL, 'Спешл')
    )

    STATUS_G = 'G'
    STATUS_PG = 'PG'
    STATUS_PG_13 = 'PG-13'
    STATUS_R_17 = 'R-17'
    STATUS_R_PLUS = 'R+'
    STATUS_R_X = 'Rx'

    STATUS_CHOICES_RATING = (
        (STATUS_G, 'G'),
        (STATUS_PG, 'PG'),
        (STATUS_PG_13, 'PG-13'),
        (STATUS_R_17, 'R-17'),
        (STATUS_R_PLUS, 'R+'),
        (STATUS_R_X, 'Rx')
    )

    types = models.CharField(max_length=100, verbose_name='Тип', choices=STATUS_CHOICES_TYPES, blank=True)
    episode = models.PositiveSmallIntegerField(verbose_name='Эпизоды', default=1)
    age_rating = models.CharField(
        max_length=100, verbose_name='Возрастной рейтинг', choices=STATUS_CHOICES_RATING, blank=True
    )
    episode_duration = models.PositiveSmallIntegerField(verbose_name='Длительность эпизода', default=0)
    studios = models.ManyToManyField(Studio, verbose_name='Студии')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Аниме'
        verbose_name_plural = 'Аниме'


class AnimeShots(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="anime_shots/")
    anime = models.ForeignKey(Anime, verbose_name="Аниме", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кадр из аниме'
        verbose_name_plural = 'Кадры из аниме'


class MangaAndLight(General):
    volume = models.PositiveSmallIntegerField(verbose_name='Том', default=1)
    chapter = models.PositiveSmallIntegerField(verbose_name='Глава', default=1)
    publisher = models.ForeignKey(Publisher, verbose_name='Издатель', on_delete=models.SET_NULL, null=True)


class Manga(MangaAndLight):
    STATUS_MANGA = 'manga'
    STATUS_MANHWA = 'manhwa'
    STATUS_MANHUA = 'manhua'
    STATUS_ONE_SHOT = 'one-shot'
    STATUS_DOUJINSHI = 'doujinshi'

    STATUS_CHOICES_TYPES = (
        (STATUS_MANGA, 'Манга'),
        (STATUS_MANHWA, 'Манхва'),
        (STATUS_MANHUA, 'Маньхуа'),
        (STATUS_ONE_SHOT, 'Ваншот'),
        (STATUS_DOUJINSHI, 'Додзиндси')
    )

    types = models.CharField(max_length=100, verbose_name='Тип', choices=STATUS_CHOICES_TYPES, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Манга'
        verbose_name_plural = 'Манга'


class Ranobe(MangaAndLight):
    STATUS_LIGHT_NOVEL = 'light novel'
    STATUS_NOVELLA = 'novella'

    STATUS_CHOICES_TYPES = (
        (STATUS_LIGHT_NOVEL, 'Ранобэ'),
        (STATUS_NOVELLA, 'Новелла')
    )

    types = models.CharField(max_length=100, verbose_name='Тип', choices=STATUS_CHOICES_TYPES, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ранобэ'
        verbose_name_plural = 'Ранобэ'