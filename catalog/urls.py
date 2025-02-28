from django.urls import path
from catalog import views
from django.views.decorators.cache import cache_page

app_name = 'catalog'

urlpatterns = [

    path('', views.ProductListView.as_view(), name='product'),
    path('contacts/', views.ContactsListView.as_view(), name='contacts'),
    path('products/', views.ProductListView.as_view(), name='product_category'),
    path('product/<int:pk>', cache_page(60)(views.ProductDetailView.as_view()), name='single'),
    path('category/', views.CategoryListView.as_view(), name='categories'),
    path('create/',views.ProductCreateView.as_view(), name='create'),
    path('product/<int:pk>/edit/',views.ProductUpdateView.as_view(), name='edit'),
    path('product/<int:pk>/delete/',views.ProductDeleteView.as_view(), name='delete')
]

# add a flag for
# handling the 404 error
handler404 = 'catalog.views.error_404_view'
