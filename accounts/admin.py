from django.contrib import admin

from accounts.models import Profile, UserPostRelation

# Register your models here.
admin.site.register(Profile)
admin.site.register(UserPostRelation)