from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from catalog.management.commands.parser import parser_xml_category, parser_xml_product
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Add test books to the database'

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()

        parser_xml_category()
        call_command('loaddata', 'catalog_fixture.xml')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from catalog fixture'))

        parser_xml_product()
        call_command('loaddata', 'product_fixture.xml')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from product fixture'))