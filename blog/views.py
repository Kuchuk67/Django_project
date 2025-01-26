from django.views.generic import DeleteView, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Article
from django.urls import reverse_lazy
from django.urls import reverse
from django import forms
from django.forms.widgets import DateTimeInput
from django.core.mail import send_mail
from django.conf import settings
from .forms import NewDataForm
from datetime import datetime
import os


# Create your views here.
class MyForm(forms.Form):
    datetime_field = forms.DateTimeField(widget=DateTimeInput(attrs={'type': 'datetime-local'}))


class BlogListView(ListView):
    model = Article
    context_object_name = 'articles'
    paginate_by = 10


    def get_queryset(self):
        dt = str(datetime.now()) + "+03:00"
        queryset = super().get_queryset()
        # фильтрация по published
        return queryset.filter(published=True, date_published__lt=dt).order_by('-date_published')


class BlogDetailView(DetailView):
    model = Article
    context_object_name = 'article'

    def get_object(self, queryset=None):
        # Получаем объект по методу get_object по умолчанию
        obj = super().get_object(queryset=queryset)
        obj.number_of_views += 1
        obj.save()
        if obj.number_of_views == 36 :
            try:
                send_mail(
                    "Новое достижение",
                    f"Статья «{obj.title}» набрала 100 просмотров",
                    settings.EMAIL_HOST_USER,
                    settings.EMAIL_HOST_SEND,
                    fail_silently=False,
                )
            except Exception as e:
                print(f'Error sending email: {e}')
            else:
                print("mail - ok")
        return obj


class BlogCreateView(LoginRequiredMixin, CreateView ):
    login_url = "/admin/login/"
    redirect_field_name = 'next'

    model = Article
    form_class = NewDataForm
    success_url = reverse_lazy('blog:articles')


class BlogUpdateView(LoginRequiredMixin, UpdateView ):
    login_url = "/admin/login/"
    redirect_field_name = 'next'
    model = Article
    fields = ['title', 'text', 'image',  'author','date_published', 'published']

    def get_success_url(self):
        return reverse('blog:article', kwargs={'pk': self.object.pk})


class BlogDeleteView(LoginRequiredMixin,  DeleteView):
    """ Удаляем запись блога"""

    def form_valid(self, form):
        # Удалить файл картинки
        if self.object.image:
            path = self.object.image.path
            os.remove(path)
        return  super().form_valid(form)

    model = Article
    context_object_name = 'article'
    success_url = reverse_lazy('blog:articles')