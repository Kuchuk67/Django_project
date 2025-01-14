from django.contrib import admin
from .models import Product, Category, PageBlock

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name')
    search_fields = ('category_name', 'description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name', 'description', 'category')
    list_filter = ('category',)


@admin.register(PageBlock)
class PageBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('author',)

