import re
from datetime import datetime
dt = datetime.now()

file_xml = '''<?xml version="1.0" encoding="utf-8"?>
<django-objects version="1.0">
'''

with  open('feed-yml.xml', 'r', encoding='utf-8') as file:
    record = False
    offer = ''
    offers = []
    i = 0
    while True:
        content = file.readline()
        if not content:
            break
        #print(content[:8])
        print('.', end="")
        if content[:10] == '<offer id=':

            #
            i +=1
            print("offer ",i)
            record = True
        if content[:8] == '</offer>':
            record = False
            offer += content
            offers.append(offer)
            offer = ''
        if record:
            offer += content


for offer in offers:
    rez = re.search('[0-9]+', offer)
    id_ = rez[0]

    rez = re.search("(Id>)([0-9]+)\<", offer)
    category_id = (rez[0])[3:-1]

    rez = re.search("(TA\[)([^}]+)]]", offer)
    description = (rez[0])[3:-2]

    rez = re.search("(name>)([^}]+)(</name)", offer)
    name = (rez[0])[5:-6]

    rez = re.search("(cture>)([^}]+)(</pict)", offer)
    img = (rez[0])[6:-6]

    rez = re.search("(rice>)([0-9]+)<", offer)
    price = int((rez[0])[5:-1])



    file_xml += f'''    <object model="catalog.product" pk="{id_}">
        <field name="name" type="CharField">{name}</field>
        <field name="description" type="TextField">{description}</field>
        <field name="image" type="FileField">{img}</field>
        <field name="category" rel="ManyToOneRel" to="catalog.category">{category_id}</field>
        <field name="price" type="IntegerField">{price}</field>
        <field name="created_at" type="DateTimeField">{dt}</field>
        <field name="updated_at" type="DateTimeField">{dt}</field>
    </object>
'''

file_xml += '</django-objects>'

with  open('product_fixture.xml', 'w', encoding='utf-8') as file:
    file.write(file_xml)


