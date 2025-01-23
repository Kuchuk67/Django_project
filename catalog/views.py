from gc import get_objects
from xml.dom import NotFoundErr

from django.shortcuts import render, get_object_or_404
from .models import  PageBlock, Product, Category
from catalog.src.new_products import new_product
from catalog.src.offset import offset_product
from django.views.generic import ListView, DetailView, TemplateView

# Create your views here.

'''def home(request,offset=1):
    """ Главная страница"""
    print(request.user)
    if offset == 0 : offset = 1
    quantity_per_page = 12
    data = new_product()
    data['products'] = Product.objects.order_by('-id').all()[(offset - 1) * quantity_per_page:offset * quantity_per_page]
    data['count'] = Product.objects.all().count()
    data['offset'],data['offset_min'],data['offset_max'] = offset_product(offset, data['count'], quantity_per_page)

    return render(request, 'home.html', context=data)
'''

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        cat = self.request.GET.get('category')
        queryset = super().get_queryset()
        if not cat:
            return queryset.all()
        return queryset.filter(category=cat)

    def get_context_data(self, **kwargs):
        """ Добавляем данные для слайдера 'Последние поступления' """
        context = super().get_context_data(**kwargs)
        context['showcase_product'] = new_product()
        return context


class ContactsListView(ListView):
    """ Страница контактов """
    model = PageBlock
    template_name = 'contacts.html'
    context_object_name = 'contact_text'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(pk=1)

    def post(self, request, *args):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name, email, message)
        return self.get(request, *args)


class ProductDetailView(DetailView):
    """ Страница карточка товара"""
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        """ Добавляем данные для слайдера 'Последние поступления' """
        context = super().get_context_data(**kwargs)
        context['showcase_product'] = new_product()
        return context


class CategoryListView(ListView):
    """ Страница категоии"""
    model = Category
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        """ Добавляем данные для слайдера 'Последние поступления' """
        context = super().get_context_data(**kwargs)
        context['showcase_product'] = new_product()
        return context


'''def category(request, pk=False, offset=1):
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
        return render(request, 'product_one_category.html', context=data)'''

def error_404_view(request, exception):
    """ Страница 404"""
    return render(request, '404.html')

