from django.contrib import admin

from posts.models import Category, Publicatie, Post

# Register your models here.
admin.site.register(Category)
admin.site.register(Publicatie)
admin.site.register(Post)