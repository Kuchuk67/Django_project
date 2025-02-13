from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, verbose_name='аватарка')
    country = models.CharField(max_length=100, verbose_name='страна', blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        """
        Ссылка на профиль
        """
        return reverse('user:profile', kwargs={'pk': self.pk})



