from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'bio', 'website']
    list_display_links = ['user']
