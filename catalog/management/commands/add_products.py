from django.core.management.base import BaseCommand
from catalog.models import Category, Product, PageBlock
from catalog.management.commands.parser import parser_xml_category, parser_xml_product
from django.core.management import call_command
from users.models import CustomUser
from datetime import datetime
dt = str(datetime.now())+ "+03:00"



class Command(BaseCommand):
    help = 'Add test books to the database'

    def handle(self, *args, **kwargs):

        Category.objects.all().delete()
        Product.objects.all().delete()
        PageBlock.objects.all().delete()




        parser_xml_category()
        call_command('loaddata', 'catalog_fixture.xml')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from catalog fixture'))

        parser_xml_product()
        call_command('loaddata', 'product_fixture.xml')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from product fixture'))

        users = CustomUser.objects.all()[:1]
        PageBlock.objects.get_or_create(id=1,
                                        title='Наши контакты',
                                        text="""<p><b>Адрес:</b> Иркутск, ул. Ленина, д. 1</p>
                                        <p><b>Телефон:</b> 8-924-123-45-76</p>
                                        <p><b>Email:</b> ddjfsf@mail.ru</p>
                                        <p><b></b></p>""",
                                        author=users[0],
                                        created_at=dt,
                                        updated_at=dt)