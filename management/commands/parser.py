import re
from datetime import datetime
dt = datetime.now()

def parser_xml_category():
    with  open('feed-yml.xml', 'r', encoding='utf-8') as file:
        list_category = []
        while True:
            content = file.readline()
            if not content:
                break
            if content[:12] == '<category id':
                rez = re.search('[0-9]+', content)
                id_ = rez[0]
                rez = re.search(r"\>([^}]+)\<", content)
                name = (rez[0])[1:-1]
                list_category.append({'id': id_, 'category_name':name})
    return list_category

def parser_xml_product():
    with  open('feed-yml.xml', 'r', encoding='utf-8') as file:
        record = False
        offer = ''
        offers = []
        i = 0
        while True:
            content = file.readline()
            if not content:
                break

            if content[:10] == '<offer id=':
                i += 1
                #print(i)
                record = True
            if content[:8] == '</offer>':
                record = False
                offer += content
                offers.append(offer)
                offer = ''
            if record:
                offer += content

    # Разбираем офферы
    list_product = []
    for offer in offers:
        rez = re.search('[0-9]+', offer)
        id_ = rez[0]

        rez = re.search("(Id>)([0-9]+)<", offer)
        category_id = (rez[0])[3:-1]

        rez = re.search("(TA\[)([^}]+)]]", offer)
        description = (rez[0])[3:-2]

        rez = re.search("(name>)([^}]+)(</name)", offer)
        name = (rez[0])[5:-6]

        # rez = re.search("(cture>)([^}]+)(</pict)", offer)
        # img = (rez[0])[6:-6]
        img = ' '  # заглушка

        rez = re.search("(rice>)([0-9]+)<", offer)
        price = int((rez[0])[5:-1])

        list_product.append({'pk': id_,
                             'name': name,
                             'description': description,
                             'image': None,
                             'category': category_id,
                             'price': price,
                             'created_at': dt,
                             'updated_at': dt
                             })
        return list_product



#print(parser_xml_category())

#print(parser_xml_product())