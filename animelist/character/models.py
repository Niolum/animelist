from django.db import models
from author.models import Author

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание', blank=True)
    photo = models.ImageField(verbose_name='Фото', upload_to='character/', blank=True)
    slug = models.SlugField(max_length=160,unique=True)
    seiyu = models.ManyToManyField(Author, verbose_name='Сэйю', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'
