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



        user = CustomUser.objects.create(
            username='admin',
            email='admin@mail.ru',
        )
        user.set_password('12345')
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()


