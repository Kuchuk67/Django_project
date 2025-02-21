from django.shortcuts import render
from .models import PageBlock, Product, Category
from catalog.src.new_products import new_product
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProductForm

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

    #extra_context = {'showcase_product': new_product()}
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["showcase_product"] = new_product()
        return context

class ProductCreateView(LoginRequiredMixin, CreateView ):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product')


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    def get_success_url(self):
        return reverse('catalog:single', kwargs={'pk': self.object.pk})


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
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
    #extra_context = {'showcase_product': new_product()}
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["showcase_product"] = new_product()
        return context

class CategoryListView(ListView):
    """ Страница категоии"""
    model = Category
    context_object_name = 'categories'

    #extra_context = {'showcase_product': new_product()}
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["showcase_product"] = new_product()
        return context


def error_404_view(request, exception):
    context = {"page_title": "404"}
    response = render(request, '404.html', context=context)
    response.status_code = 404
    return response
