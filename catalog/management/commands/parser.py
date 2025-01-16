import re
import os
from datetime import datetime
from config.settings import BASE_DIR

file_xml_name = os.path.join(BASE_DIR,'catalog', 'management', 'commands', 'feed-yml.xml')


def parser_xml_category():
    """ Функция создает фикстуру категорий из файла XML Яндекс-маркета feed-yml.xml
    Сохраняет в файл catalog_fixture.xml в корне проекта
    """
    file_xml = '''<?xml version="1.0" encoding="utf-8"?>
    <django-objects version="1.0">
    '''
    with  open(file_xml_name, 'r', encoding='utf-8') as file:
        while True:
            content = file.readline()
            if not content:
                break

            if content[:12] == '<category id':
                rez = re.search('[0-9]+', content)
                id = rez[0]
                rez = re.search(r"\>([^}]+)\<", content)
                name = (rez[0])[1:-1]
                file_xml += f'''    <object model="catalog.category" pk="{id}">
            <field name="category_name" type="CharField">{name}</field>
            <field name="description" type="TextField"> </field>
        </object>'''
    file_xml += '</django-objects>'
    with  open('catalog_fixture.xml', 'w', encoding='utf-8') as file:
        file.write(file_xml)


def parser_xml_product():
    """ Функция создает фикстуру продуктов из файла XML Яндекс-маркета feed-yml.xml
    Сохраняет в файл product_fixture.xml в корне проекта
        """
    file_xml = '''<?xml version="1.0" encoding="utf-8"?>
    <django-objects version="1.0">
    '''

    with  open(file_xml_name, 'r', encoding='utf-8') as file:
        record = False
        offer = ''
        offers = []
        i = 0
        while True:
            content = file.readline()
            if not content:
                break

            #print('.', end="")
            if content[:10] == '<offer id=':
                i += 1
                #print("offer ", i)
                record = True
            if content[:8] == '</offer>':
                record = False
                offer += content
                offers.append(offer)
                offer = ''
            if record:
                offer += content

    for offer in offers:
        dt = datetime.now()
        rez = re.search('[0-9]+', offer)
        id_ = rez[0]

        rez = re.search("(Id>)([0-9]+)<", offer)
        category_id = (rez[0])[3:-1]

        rez = re.search("(DATA)([^}]+)]]", offer)
        description = (rez[0])[5:-2]

        rez = re.search("(name>)([^}]+)(</name)", offer)
        name = (rez[0])[5:-6]

        # rez = re.search("(cture>)([^}]+)(</pict)", offer)
        # img = (rez[0])[6:-6]
        img = ' '  # заглушка
        if int(id_) in [25086,27626,27738,27783,27834,28094,28328,28483,27431,27181]:
            img = 'images_products/'+str(id_)+'.png'
        rez = re.search("(rice>)([0-9]+)<", offer)
        price = int((rez[0])[5:-1])

        file_xml += f'''    <object model="catalog.product" pk="{id_}">
            <field name="name" type="CharField">{name}</field>
            <field name="description" type="TextField">{description}</field>
            <field name="image" type="FileField">{img}</field>
            <field name="category" rel="ManyToOneRel" to="catalog.category">{category_id}</field>
            <field name="price" type="IntegerField">{price}</field>
            <field name="created_at" type="DateTimeField">{dt}+03:00</field>
            <field name="updated_at" type="DateTimeField">{dt}+03:00</field>
        </object>
    '''

    file_xml += '</django-objects>'

    with  open('product_fixture.xml', 'w', encoding='utf-8') as file:
        file.write(file_xml)



print(parser_xml_category())
print(parser_xml_product())