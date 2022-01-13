from django.db import models

# Create your models here.
class Common(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=160, unique=True)


class Publisher(Common):

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'


class Studio(Common):
    logo = models.ImageField(verbose_name='Логотип', upload_to='studios/', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Студия'
        verbose_name_plural = 'Студии'
