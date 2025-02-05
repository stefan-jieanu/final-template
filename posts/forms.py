from django.forms import ModelForm

from posts.models import Post, Review


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'description']