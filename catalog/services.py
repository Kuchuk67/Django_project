from itertools import product

from config.settings import CACHES_ENABLED
from catalog.views import Product


def get_product_from_cache():
    """ Функция возвращает список товаров из кэша, если он включен """
    if CACHES_ENABLED:
        from django.core.cache import cache
        products = cache.get('products')
        if products:
            return products
        else:
            products = Product.objects.all()
            cache.set('products', products, 60)  # 1 минута
            return products
    else:
        return Product.objects.all()


