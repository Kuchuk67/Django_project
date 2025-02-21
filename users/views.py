from .forms import SignUpForm, UserUpdateForm
from django.urls import reverse_lazy
from .models import CustomUser
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
class SignUpView(CreateView):
    model = CustomUser
    form_class = SignUpForm
    success_url = reverse_lazy('users:login')
    template_name ='register.html'


    @staticmethod
    def message_to(mail_to):
        send_mail(
            "Регистрация на сайте «Цифровая техника»",
            f"""Вы успешно зарегистрированы на сайте «Цифровая техника»
Ваш логин e-mail: {mail_to}""",
            settings.EMAIL_HOST_USER,
            (mail_to,),
            fail_silently=False,
        )

    def form_valid(self, form):
        self.message_to(self.request.POST.get('email'))
        return super().form_valid(form)





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
    path_img_temp = None

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.image:
            self.path_img_temp = self.object.image.path

        return super().post(request, *args, **kwargs)


    def form_valid(self, form):
        # Удалить файл картинки
        if not self.object.image and self.path_img_temp:
            os.remove(self.path_img_temp)
        return  super().form_valid(form)


    # Определяем текущего пользователя и грузим только его
    def get_object(self, queryset=None):
        queryset = self.get_queryset()
        queryset = queryset.filter(pk=self.request.user.pk)
        return queryset.get()


    def get_success_url(self):
        return reverse('catalog:product')







