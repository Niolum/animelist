from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    STATUS_MALE = 'male'
    STATUS_FEMALE = 'female'

    STATUS_CHOICES = (
        (STATUS_MALE, 'мужчина'),
        (STATUS_FEMALE, 'женщина')
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name='Пользователь', on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name='Фото', upload_to='users/%Y/%m/%d', blank=True)
    gender = models.CharField(max_length=100, verbose_name='Пол', choices=STATUS_CHOICES, blank=True)
    date_of_birth = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    
    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'