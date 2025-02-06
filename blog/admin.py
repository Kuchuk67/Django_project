from django.contrib import admin
from .models import Article

# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published', 'published')
    search_fields = ('title', 'date_published')
    list_filter = ('author', 'created_at')


