
from . import views
from django.urls import path

app_name = 'catalog'

urlpatterns = [
    #path('home/', views.home, name='home'),
    path('<int:offset>', views.home, name='home'),
    path('', views.home, name='index_home'),
    path('contacts/', views.contacts, name='contacts'),
    path('product/<int:pk>', views.single, name='single'),
    path('category/<int:pk>', views.category, name='category'),
    path('category/', views.category, name='categories'),
]

# add a flag for
# handling the 404 error
handler404 = 'catalog.views.error_404_view'
