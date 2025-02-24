from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from .models import PageBlock, Product, Category
from catalog.src.new_products import new_product
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProductForm, ProductModeratorForm
from django.db.models import Q

# Create your views here.


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 12

    # Фильтрация и сортировка товаров на странице
    def get_queryset(self):
        queryset = super().get_queryset()
        # параметры сортировки - передается в гет запросе, например: &sort=-price
        if sort := self.request.GET.get('sort'):
            sort = sort.split(',')
        else:
            sort = ['-id']

        #  Динамическая фильтрация
        FILTER = {}
        # Фильтрайия по категориям
        if cat := self.request.GET.get('category'):
            FILTER['category'] = cat

        user = self.request.user
        # если пользователь суперюзер или модератор ему показываются все товары.
        # иначе только опубликованные
        if not user.is_superuser and not user.has_perm('catalog.can_unpublish_product'):
            return queryset.filter(**FILTER).filter(Q(unpublish_product='published') | Q(owner=user.pk)).order_by(*sort)
        return queryset.filter(**FILTER).order_by(*sort)


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["showcase_product"] = new_product()
        return context

class ProductCreateView(LoginRequiredMixin, CreateView ):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product')


    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(ProductCreateView, self).form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    #form_class = ProductForm
    def get_success_url(self):
        return reverse('catalog:single', kwargs={'pk': self.object.pk})


    def get_form_class(self):
        user = self.request.user
        # Редактировать только свои товары или если ты суперюзер
        if user == self.object.owner or user.is_superuser:
            return ProductForm
        # если модератор открыть unpublish_product
        elif user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm
        else:
            return PermissionDenied




class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product')

    def get(self,  *args, **kwargs):
        user = self.request.user
        product = Product.objects.get(pk=kwargs['pk'])
        # Удалить можно если
        # этот продукт текущего пользователя
        # пользователь в группе модераторы
        # пользователь с правами суперюзера
        if user.pk == product.owner_id or user.is_superuser or user.has_perm('catalog.can_unpublish_product'):
            return super().get(*args, **kwargs)
        raise PermissionDenied()


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
        #print(name, email, message)
        return self.get(request, *args)


class ProductDetailView(DetailView):
    """ Страница карточка товара"""
    model = Product
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["showcase_product"] = new_product()
        return context

class CategoryListView(ListView):
    """ Страница категоии"""
    model = Category
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["showcase_product"] = new_product()
        return context


def error_404_view(request, exception):
    context = {"page_title": "404"}
    response = render(request, '404.html', context=context)
    response.status_code = 404
    return response
