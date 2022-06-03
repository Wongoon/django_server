from django.contrib import admin
from .models import Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    search_fields = ['subject']
admin.site.register(Blog, BlogAdmin)
