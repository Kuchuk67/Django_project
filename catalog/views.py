from gc import get_objects
from xml.dom import NotFoundErr

from django.shortcuts import render, get_object_or_404
from .models import PageBlock, Product, Category
from catalog.src.new_products import new_product
from catalog.src.offset import offset_product
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 12

    # Фильтрация и сортировка товаров на странице
    def get_queryset(self):
        queryset = super().get_queryset()
        # параметры сортировки
        if sort := self.request.GET.get('sort'):
            sort = sort.split(',')
        else:
            sort = ['-id']
        # фильтрация по категориям
        if cat := self.request.GET.get('category'):
            return queryset.filter(category=cat).order_by(*sort)
        return queryset.all().order_by(*sort)

    extra_context = {'showcase_product': new_product()}


class ProductCreateView(LoginRequiredMixin, CreateView ):
    login_url = "/admin/"
    #redirect_field_name = "redirect_to"

    model = Product
    fields = ['name', 'description', 'image', 'category', 'price']
    success_url = reverse_lazy('catalog:product')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'image', 'category', 'price']
    success_url = reverse_lazy('catalog:product')


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
    extra_context = {'showcase_product': new_product()}


class CategoryListView(ListView):
    """ Страница категоии"""
    model = Category
    context_object_name = 'categories'

    extra_context = {'showcase_product': new_product()}


def error_404_view(request, exception):
    """ Страница 404"""
    return render(request, '404.html')
