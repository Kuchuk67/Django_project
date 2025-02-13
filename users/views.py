from django.views.generic import CreateView
from .forms import SignUpForm
from django.urls import reverse_lazy
from .models import CustomUser



# Create your views here.
class SignUpView(CreateView):

    model = CustomUser
    form_class = SignUpForm
    success_url = reverse_lazy('catalog:product')
    template_name ='register.html'




