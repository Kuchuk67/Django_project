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
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control',})
        self.fields['price'].widget.attrs.update({'class': 'form-control',})
        self.fields['description'].widget.attrs.update({'class': 'form-control','placeholder': 'Введите описание товара'})
        self.fields['category'].widget.attrs.update({'class': 'form-control',})
        self.fields['image'].widget.attrs.update({'class': 'form-control',})



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

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError('Цена не может быть отрицательной.')
        return price

    def clean_image(self):
        image = self.cleaned_data['image']
        if type(image) is not bool and hasattr(image, 'size'):
            if image.size > 1024 * 1024:  # 1MB
                raise forms.ValidationError('Изображение не может быть больше 1MB.')
        return image


