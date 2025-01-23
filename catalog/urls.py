
from . import views
from django.urls import path
from .views import CategoryListView, ProductDetailView
from .models import Category

app_name = 'catalog'

urlpatterns = [
    #path('home/', views.home, name='home'),
    path('<int:offset>', views.home, name='home'),
    path('', views.home, name='index_home'),
    path('contacts/', views.contacts, name='contacts'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='single'),
    path('category/<int:pk>', views.category, name='category'),
    #path('category/', views.category, name='categories'),
    path('category/', CategoryListView.as_view(), name='categories'),
]

# add a flag for
# handling the 404 error
handler404 = 'catalog.views.error_404_view'
