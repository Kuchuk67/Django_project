from django.db import models

from users.models import CustomUser
from django.core.validators import FileExtensionValidator
# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='категория')
    description = models.TextField(verbose_name='описание', null=True, blank=True, )
    image = models.ImageField(upload_to='images_cat/',  null=True, blank=True, verbose_name='изображение')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['category_name']

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='images_products/',
                              null=True,
                              blank=True,
                              validators=[FileExtensionValidator(['png','jpg'])],
                              verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    price = models.IntegerField( verbose_name='цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')
    owner =models.ForeignKey(CustomUser, verbose_name='Автор', on_delete=models.PROTECT)
    STATUS_CHOICES = [
        ('published', 'Опубликовано'),
        ('unpublished', 'Остановлено'),
        ('pending', 'На утверждении'),
     ]
    unpublish_product = models.CharField(max_length=17, verbose_name='наименование', choices=STATUS_CHOICES, default='pending')

    """def save(self, *args, **kwargs):
        self.owner = self.request.user.id
        super(Product, self).save(*args, **kwargs)"""

    def __str__(self):
        return f'{self.name} - {self.price}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['created_at']
        permissions = [
            ('can_unpublish_product','Может отменять публикацию продукта')
        ]


class PageBlock(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название блока')
    text = models.TextField(verbose_name='текстовой блок', null=True, blank=True, )
    author = models.ForeignKey(CustomUser, verbose_name='Автор', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='дата последнего изменения')


    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'Текстовой Блок'
        verbose_name_plural = 'Текстовые Блоки'
        ordering = ['created_at']