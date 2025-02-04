from lib2to3.fixes.fix_input import context

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from accounts.models import UserPostRelation
from posts.forms import PostForm
from posts.models import Post, Review


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

# class PostDetails(DetailView):
#     model = Post
#     template_name = 'posts_detail.html'

def post_detail_view(request, pk):
    post = Post.objects.get(pk=pk)
    reviews = Review.objects.filter(post=post)
    return render(
        request,
        'posts_detail.html',
        context = {
            'object': post,
            'reviews': reviews
        }
    )

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

def add_review_view(request, post_id):
    if request.method == 'POST':
        rating = request.POST['rating']
        comment = request.POST['comment']
        post = Post.objects.get(pk=post_id)

        Review.objects.create(
            rating=rating,
            description=comment,
            post=post,
            user=request.user
        )

        return redirect('posts-detail', pk=post_id)
    else:
        return redirect('posts-page')