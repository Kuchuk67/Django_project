from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='категория')
    description = models.TextField(verbose_name='описание')


    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['category_name']

class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(upload_to='images_products/', null=True, blank=True, verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    price = models.IntegerField( verbose_name='цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='дата последнего изменения')


    def __str__(self):
        return f'{self.name} - {self.price}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['created_at']

