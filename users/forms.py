from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
import re

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [ 'email', 'password1', 'password2']


    def __init__(self, *args, **kwargs):
        """ Обновление стилей формы обновления  """
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control', })
        self.fields['password1'].widget.attrs.update({'class': 'form-control', })
        self.fields['password2'].widget.attrs.update({'class': 'form-control', })

    # Проверка уникальности полей
    def clean_email(self):
        email = self.cleaned_data['email']
        print('========', email)
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Такой e-mail уже существует')
        return email


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
        self.fields['number_phone'].widget.attrs.update({'class': 'form-control', })

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'avatar',  'country', 'number_phone']

    def clean_number_phone(self):
        number_phone = self.cleaned_data['number_phone']
        number_phone = ''.join(re.findall('[0-9]', number_phone))
        if len(number_phone) < 8:
            raise forms.ValidationError('Номер телефона должен содержать минимум 8 цифр')
        return number_phone



