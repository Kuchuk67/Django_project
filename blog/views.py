from django.shortcuts import render
from django.views.generic import DeleteView, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Article
from django.urls import reverse_lazy
from django.urls import reverse
from django import forms
from django.forms.widgets import DateInput, DateTimeInput
from django.core.mail import send_mail
from django.conf import settings
from .forms import NewDataForm
from datetime import datetime


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
        #return queryset.all().order_by(*sort)


class BlogDetailView(DetailView):
    model = Article
    context_object_name = 'article'

    def get_object(self, queryset=None):
        # Получаем объект по методу get_object по умолчанию
        obj = super().get_object(queryset=queryset)
        obj.number_of_views += 1
        obj.save()
        if obj.number_of_views == 32 :
            try:
                send_mail(
                    "Новое достижение",
                    f"Статья «{obj.title}» набрала 100 просмотров",
                    "kuchukov.sergey@gmail.com",
                    ["kuchukov.s@mail.ru"],
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
    #fields = ['title', 'text', 'image',  'author','date_published', 'published']
    success_url = reverse_lazy('blog:articles')


class BlogUpdateView(LoginRequiredMixin, UpdateView ):
    login_url = "/admin/login/"
    redirect_field_name = 'next'

    model = Article
    #form_class = NewDataForm
    #
    fields = ['title', 'text', 'image',  'author','date_published', 'published']

    def get_success_url(self):
        return reverse('blog:article', kwargs={'pk': self.object.pk})


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('blog:articles')
