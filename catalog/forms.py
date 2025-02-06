from django import forms
from.models import Product

class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.stop_words = ['казино',
                           'криптовалюта',
                           'крипта',
                           'биржа',
                           'дешево',
                           'бесплатно',
                           'обман',
                           'полиция',
                           'радар',
                           ]
        super().__init__(*args, **kwargs)


    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'category', 'image')


    def clean_name(self):
        name = self.cleaned_data['name']

        for stop_word in self.stop_words:
            if stop_word in name.lower():
                raise forms.ValidationError('Название продукта не должно содержать стоп-слов.')
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        for stop_word in self.stop_words:
            if stop_word in description.lower():
                raise forms.ValidationError('Название продукта не должно содержать стоп-слов.')
        return description