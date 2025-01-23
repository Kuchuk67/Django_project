
from . import views
from django.urls import path
from .views import CategoryListView, ProductDetailView, ContactsListView, ProductListView
from .models import Category

app_name = 'catalog'

urlpatterns = [
    #path('home/', views.home, name='home'),
    #path('<int:offset>', views.home, name='home'),
    path('', ProductListView.as_view(), name='product'),
    path('contacts/', ContactsListView.as_view(), name='contacts'),
    path('products/', ProductListView.as_view(), name='product_category'),
    #/products/?category=
    path('product/<int:pk>', ProductDetailView.as_view(), name='single'),
    #path('category/<int:pk>', views.category, name='category'),
    #path('category/', views.category, name='categories'),
    path('category/', CategoryListView.as_view(), name='categories'),
]

# add a flag for
# handling the 404 error
handler404 = 'catalog.views.error_404_view'
