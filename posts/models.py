from django.db import models
from django.db.models import Model, TextField, ForeignKey, DO_NOTHING, DateTimeField, CharField, ManyToManyField


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
    created = DateTimeField
    publications = ManyToManyField(Publicatie)

    def __str__(self):
        return self.title