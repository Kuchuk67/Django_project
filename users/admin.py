from django.contrib import admin
from .models import CustomUser

# Register your models here.
"""@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'email')
    search_fields = ('name', 'email')
    list_filter = ('category',)"""
