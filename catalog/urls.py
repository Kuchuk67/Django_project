
from . import views
from django.urls import path
from catalog import views

app_name = 'catalog'

urlpatterns = [
    #path('home/', views.home, name='home'),
    #path('<int:offset>', views.home, name='home'),
    path('', views.ProductListView.as_view(), name='product'),
    path('contacts/', views.ContactsListView.as_view(), name='contacts'),
    path('products/', views.ProductListView.as_view(), name='product_category'),
    #/products/?category=
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='single'),
    #path('category/<int:pk>', views.category, name='category'),
    #path('category/', views.category, name='categories'),
    path('category/', views.CategoryListView.as_view(), name='categories'),
    path('create/',views.ProductCreateView.as_view(), name='create')
]

# add a flag for
# handling the 404 error
handler404 = 'catalog.views.error_404_view'
