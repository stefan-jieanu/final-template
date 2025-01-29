from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from posts.forms import PostForm
from posts.models import Post

# Create your views here.
def index(request):
    return render(request, 'home.html')

def posts_view(request):
    posts = Post.objects.all()

    return render(
        request,
        'posts.html',
        context={'posts': posts}
    )

class PostDetails(DetailView):
    model = Post
    template_name = 'posts_detail.html'

class CreatePostView(CreateView):
    model = Post
    template_name = 'posts_create.html'
    form_class = PostForm
    success_url = reverse_lazy('posts-page')