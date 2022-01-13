from django.db import models

# Create your models here.
class Role(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    date_of_birth = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    roles = models.ManyToManyField(Role, verbose_name='Роли')
    photo = models.ImageField(verbose_name='Фото', upload_to='authors/', blank=True)
    slug = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    

