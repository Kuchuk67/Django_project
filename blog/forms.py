from django import forms
from .models import Article
class NewDataForm(forms.ModelForm):
    class Meta:
        model = Article
        widgets = {"date_published": forms.DateTimeInput(attrs={'type':'datetime-local'}) }
        fields = '__all__'