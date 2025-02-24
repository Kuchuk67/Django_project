from django.core.management.base import BaseCommand
from users.models import CustomUser
from blog.models import Article
from catalog.models import Category, Product, PageBlock
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):


    def handle(self, *args, **kwargs):

        # Создаем новую группу
        new_group, created = Group.objects.get_or_create(name='Модератор продуктов')

        print('Создаем новую группу', new_group, created)
        ct = ContentType.objects.get_for_model(Product)
        model_add_perm = Permission.objects.get(name ='Может отменять публикацию продукта', codename ='can_unpublish_product', content_type = ct)
        new_group.permissions.add(model_add_perm)
        print("Подключили can_unpublish")



        user2 = CustomUser.objects.create(
            username='Модератор Василий',
            email='moder@mail.ru',
        )
        user2.set_password('12345')
        user2.groups.add(new_group)
        user2.save()

        # Создаем новую группу
        new_group, created = Group.objects.get_or_create(name='Пользователь')
        print('Создаем новую группу', new_group, created)


        user3 = CustomUser.objects.create(
            username='User',
            email='user@mail.ru',
        )
        user3.set_password('12345')
        user3.groups.add(new_group)
        user3.save()

#asdsDD24#$re
