from .forms import SignUpForm, UserUpdateForm
from django.urls import reverse_lazy
from .models import CustomUser
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class SignUpView(CreateView):

    model = CustomUser
    form_class = SignUpForm
    success_url = reverse_lazy('users:login')
    template_name ='register.html'


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser
    success_url = reverse_lazy('catalog:product')
    template_name = 'profile.html'


    # Определяем текущего пользователя и грузим только его
    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        queryset = queryset.filter(pk=self.request.user.pk)
        return queryset.get()


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UserUpdateForm
    success_url = reverse_lazy('users:profile')
    template_name = 'profile_edite.html'


    # Определяем текущего пользователя и грузим только его
    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        queryset = queryset.filter(pk=self.request.user.pk)
        return queryset.get()


    def get_success_url(self):
        return reverse('catalog:product')







