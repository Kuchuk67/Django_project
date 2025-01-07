
from . import views
from django.urls import path

app_name = 'catalog'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.home, name='index_home'),
    path('contacts/', views.contacts, name='contacts'),

]
