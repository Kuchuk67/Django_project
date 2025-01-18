from catalog.models import Category, Product

def new_product() -> dict:
    """ Вернет из какждой категории по одному последнему продукту
    Возвращает словарь с ключом ID продуктов и значение: словарь с данными"""
    all_cat =  Category.objects.all()
    data = {}
    dict_products = {}
    data_showcase_id = []
    for category in all_cat:
        #print(category.id)
        products = Product.objects.order_by('-id').filter( category=category.id)[:1] #
        for product in products:
            dict_products[product.id] = {'name': product.name,
                                         'description': product.description,
                                         'image': product.image,
                                         'price': product.price,
                                         'id': product.id,}
            data_showcase_id.append(product.id)
        sorted_dict_products = dict(sorted(dict_products.items(), reverse=True))
        i = 0


        for value in sorted_dict_products.values():
            i+=1
            # data_showcase.append([value['id'], value['name'], value['description'], value['image'], value['price']])
            data['name'+str(i)] = value['name']
            data['description' + str(i)] = value['description']
            data['image' + str(i)] = value['image']
            data['price' + str(i)] = value['price']
            data['id' + str(i)] = value['id']
            if i == 9:
                break


    data_showcase_id.sort(reverse=True)
    data['showcase_product'] = []
    data['showcase_product'].append(Product.objects.filter(id__in = data_showcase_id[0:3]))
    data['showcase_product'].append(Product.objects.filter(id__in=data_showcase_id[3:6]))
    data['showcase_product'].append(Product.objects.filter(id__in=data_showcase_id[6:9]))
    return data


def data_product() -> dict:
    ...
