import re

file_xml = '''<?xml version="1.0" encoding="utf-8"?>
<django-objects version="1.0">
'''

with  open('feed-yml.xml', 'r', encoding='utf-8') as file:

    while True:
        content = file.readline()
        if not content:
            break
        #print(content[:12])
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

#with  open('catalog_fixture.xml', 'w', encoding='utf-8') as file:
 #   file.write(file_xml)

from datetime import datetime
print(datetime.now())
# 2025-01-13T19:02:10.793187+00:00