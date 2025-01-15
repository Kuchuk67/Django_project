from catalog.models import Category, Product

def new_product() -> dict:
    """ Вернет из какждой категории по одному последнему продукту
    Возвращает словарь с ключом ID продуктов и значение: словарь с данными"""
    all_cat =  Category.objects.all()
    data = {}
    dict_products = {}
    for category in all_cat:
        #print(category.id)
        products = Product.objects.order_by('-id').filter( category=category.id)[:1] #
        for product in products:
            dict_products[product.id] = {'name': product.name,
                                         'description': product.description,
                                         'image': product.image,
                                         'price': product.price,
                                         'id': product.id,}

        sorted_dict_products = dict(sorted(dict_products.items(), reverse=True))
        i = 0

        for value in sorted_dict_products.values():
            i+=1
            data['name'+str(i)] = value['name']
            data['description' + str(i)] = value['description']
            data['image' + str(i)] = value['image']
            data['price' + str(i)] = value['price']
            data['id' + str(i)] = value['id']
            if i == 9:
                break

    return data
    #return sorted(dict_products, reverse=True)

def data_product() -> dict:
    ...
