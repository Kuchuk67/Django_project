from django.views.generic import CreateView
from .forms import SignUpForm, UserUpdateForm
from django.urls import reverse_lazy
from .models import CustomUser
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# Create your views here.
class SignUpView(CreateView):

    model = CustomUser
    form_class = SignUpForm
    success_url = reverse_lazy('users:login')
    template_name ='register.html'

class ProfileDetailView(DetailView):
    model = CustomUser
    success_url = reverse_lazy('catalog:product')
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        #context['title'] = f'Страница пользователя: {self.object.user.username}'
        print(context['object'].email)
        return context

class ProfileUpdateView(UpdateView):
    model = CustomUser
    form_class = UserUpdateForm
    success_url = reverse_lazy('users:profile')
    template_name = 'profile_edite.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)







