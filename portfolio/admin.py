from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Post, Category, Tag, Portfolio

admin.site.register(Post)
admin.site.register(Portfolio)
admin.site.register(Category)
admin.site.register(Tag)


