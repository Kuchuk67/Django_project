from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('blog/', views.BlogListView.as_view(), name='articles'),
    path('blog/article/<int:pk>', views.BlogDetailView.as_view(), name='article'),
    path('blog/creat/', views.BlogCreateView.as_view(), name='create'),
    path('blog/article/<int:pk>/update/', views.BlogUpdateView.as_view(), name='update'),
    path('blog/article/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='delete'),
]