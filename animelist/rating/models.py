from django.db import models
from main.models import General

# Create your models here.
class Ratingstar(models.Model):
    value = models.SmallIntegerField('Значение', default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'
        ordering = ['-value']


class Rating(models.Model):
    ip = models.CharField(max_length=15, verbose_name='IP адрес')
    star = models.ForeignKey(Ratingstar, verbose_name='Звезда', on_delete=models.CASCADE)
    general = models.ForeignKey(General, verbose_name='Произведение', related_name='ratings', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.star}-{self.general}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'