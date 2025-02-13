from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [ 'email', 'password1', 'password2']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm'}),
        }
        help_texts = {
            'password1': ('Пароль должен содержать как минимум 8 символов, включая буквы в верхнем и нижнем регистре, цифры и специальные символы.'),
            'password2': ('Пароли должны совпадать.'),
        }

class UserUpdateForm(forms.ModelForm):
    """
    Форма обновления данных пользователя
    """
    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы обновления
        """
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', })
        self.fields['email'].widget.attrs.update({'class': 'form-control', })
        self.fields['country'].widget.attrs.update({'class': 'form-control', })
        self.fields['avatar'].widget.attrs.update({'class': 'form-control', })


    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'avatar',  'country']




