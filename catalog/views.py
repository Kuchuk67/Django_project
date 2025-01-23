from gc import get_objects
from xml.dom import NotFoundErr

from django.shortcuts import render, get_object_or_404
from .models import  PageBlock, Product, Category
from catalog.src.new_products import new_product
from catalog.src.offset import offset_product
from django.views.generic import ListView, DetailView, TemplateView

# Create your views here.



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

    extra_context = {'showcase_product': new_product() }


class ContactsListView(ListView):
    """ Страница контактов """
    model = PageBlock
    template_name = 'catalog/contacts.html'
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
    extra_context = {'showcase_product': new_product() }


class CategoryListView(ListView):
    """ Страница категоии"""
    model = Category
    context_object_name = 'categories'

    extra_context = {'showcase_product': new_product() }


def error_404_view(request, exception):
    """ Страница 404"""
    return render(request, '404.html')

