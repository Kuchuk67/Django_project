from django import forms
from .models import Article

"""class NewDataForm(forms.ModelForm):
    class Meta:
        model = Article
        widgets = {"date_published": forms.DateTimeInput(attrs={'type':'datetime-local'}) }
        fields = ['title', 'text', 'image',  'author','date_published', 'published']
"""

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Article
        widgets = {"date_published": forms.DateTimeInput(attrs={'type': 'datetime-local'})}
        fields = ['title', 'text', 'image',  'author','date_published', 'published']

    def __init__(self, *args, **kwargs):
        super(BlogPostForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': 'form-control', })
        self.fields['text'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите текст статьи'})
        self.fields['image'].widget.attrs.update({'class': 'form-control', })
        self.fields['author'].widget.attrs.update({'class': 'form-control', })
        self.fields['date_published'].widget.attrs.update({'class': 'form-control', 'type':'datetime-local'})
        self.fields['published'].widget.attrs.update({'class': 'form-control', 'type':'checkbox'})



