from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, verbose_name='Имя', blank=True, unique=False)

    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, verbose_name='аватарка')
    country = models.CharField(max_length=100, verbose_name='страна', blank=True)
    number_phone = models.CharField(max_length=20, verbose_name='телефон', blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email









