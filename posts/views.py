from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from accounts.models import UserPostRelation
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

@login_required
def add_post_to_user(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(pk=post_id)
        rel = UserPostRelation.objects.create(user=request.user, post=post)
        return redirect('posts-page')
    else:
        return redirect('posts-page')