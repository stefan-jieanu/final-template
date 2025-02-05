from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model, TextField, ForeignKey, DO_NOTHING, DateTimeField, CharField, ManyToManyField, \
    IntegerField, CASCADE


# Create your models here.
class Category(Model):
    class Meta:
        verbose_name_plural = 'Categories'

    title = CharField(max_length=128)
    description = TextField()

    def __str__(self):
        return self.title


class Publicatie(Model):
    name = CharField(max_length=128)
    description = TextField()

    def __str__(self):
        return self.name


class Post(Model):
    title = CharField(max_length=128)
    description = TextField()
    category = ForeignKey(Category, on_delete=DO_NOTHING)
    created = DateTimeField(auto_now_add=True)
    publications = ManyToManyField(Publicatie)

    def __str__(self):
        return self.title


class Review(Model):
    rating = IntegerField()
    description = CharField(max_length=200, blank=True, null=True)
    post = ForeignKey(Post, on_delete=CASCADE)
    user = ForeignKey(User, on_delete=CASCADE)
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review pentru {self.post.title}, adaugat de {self.user.username}'