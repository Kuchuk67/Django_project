from django.core.management.base import BaseCommand
from users.models import CustomUser
from blog.models import Article
from catalog.models import Category, Product, PageBlock


class Command(BaseCommand):


    def handle(self, *args, **kwargs):
        Article.objects.all().delete()
        Category.objects.all().delete()
        Product.objects.all().delete()
        PageBlock.objects.all().delete()

        CustomUser.objects.all().delete()

        CustomUser.objects.get_or_create(
            pk=1,
            username='admin',
            email='admin@mail.ru',
            password='12345',
            is_staff=True,
            is_superuser=True,
        )

        CustomUser.objects.get_or_create(
            pk=2,
            username='Модератор Василий',
            email='moder@mail.ru',
            password='12345',
        )
        CustomUser.objects.get_or_create(
            pk=3,
            username='User',
            email='user@mail.ru',
            password='12345',
        )

#asdsDD24#$re
