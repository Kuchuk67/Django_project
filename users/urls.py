from django.urls import path
from users.views import SignUpView
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'users'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name = "login.html"), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    #path('profile/', views.ProfileView.as_view(), name='profile'),
]