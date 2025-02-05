from django.contrib import admin

from posts.models import Category, Publicatie, Post, Review

# Register your models here.
admin.site.register(Category)
admin.site.register(Publicatie)
admin.site.register(Post)
admin.site.register(Review)