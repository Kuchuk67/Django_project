from gc import get_objects
from xml.dom import NotFoundErr

from django.shortcuts import render, get_object_or_404
from .models import  PageBlock, Product, Category
from catalog.src.new_products import new_product
from catalog.src.offset import offset_product

# Create your views here.

def home(request,offset=1):
    """ Главная страница"""
    print(request.user)


    if offset == 0 : offset = 1
    quantity_per_page = 12
    data = new_product()
    data['products'] = Product.objects.order_by('-id').all()[(offset - 1) * quantity_per_page:offset * quantity_per_page]
    data['count'] = Product.objects.all().count()
    data['offset'],data['offset_min'],data['offset_max'] = offset_product(offset, data['count'], quantity_per_page)

    return render(request, 'home.html', context=data)


def contacts(request):
    """ Страница контактов"""
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name, email, message)
        request.status_post = True
    else:
        request.status_post = False

    b_tests = PageBlock.objects.filter(id=1)
    data_c = {"contacts_title": '', "contacts_txt": ''}
    for x in b_tests:
        data_c = {"contacts_title": x.title, "contacts_txt": x.text}

    return render(request, 'contacts.html', context=data_c)

def single(request,pk=False):
    """ Страница карточка товара"""
    data = new_product()
    data['product'] = get_object_or_404(Product, id=pk)
    return render(request, 'product_single.html', context=data)


def category(request, pk=False, offset=1):
    """ Страница категорий товаров"""
    # если не выбрана категория
    if not pk:
        data = new_product()
        data['categories'] = Category.objects.all()
        return render(request, 'category.html', context=data)
    # выбрана категория pk
    else:
        data = new_product()
        quantity_per_page = 12
        data['products'] = Product.objects.order_by('-id').filter(category=pk)[
                           (offset - 1) * quantity_per_page:offset * quantity_per_page]
        data['count'] = Product.objects.filter(category=pk).count()
        data['offset'], data['offset_min'], data['offset_max'] = offset_product(offset, data['count'],
                                                                                quantity_per_page)
        category = Category.objects.get(pk=pk)
        data['title'] = category.category_name
        return render(request, 'product_one_category.html', context=data)

def error_404_view(request, exception):
    """ Страница 404"""
    return render(request, '404.html')

