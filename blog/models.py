from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название статьи')
    text = models.TextField(verbose_name='статья', null=True, blank=True, )
    image = models.ImageField(upload_to='images_aticle/',  null=True, blank=True, verbose_name='превью статьи')
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.PROTECT , related_name="user")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')
    date_published = models.DateTimeField( verbose_name='дата публикации')
    published = models.BooleanField(default=True,verbose_name='Опубликовано')
    number_of_views = models.IntegerField(default=0,verbose_name='Количество просмотров')


    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'Статья>'
        verbose_name_plural = 'Статьи'
        ordering = ['-date_published']
