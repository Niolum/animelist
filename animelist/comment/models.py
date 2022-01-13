from django.db import models
from user.models import Profile
from main.models import General

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(Profile, verbose_name='Пользователь', on_delete=models.CASCADE)
    general = models.ForeignKey(General, verbose_name='Произведение', on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(verbose_name='Сообщение')
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'