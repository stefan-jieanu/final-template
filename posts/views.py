from lib2to3.fixes.fix_input import context

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from accounts.models import UserPostRelation
from posts.forms import PostForm, ReviewForm
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
    reviews = Review.objects.filter(post=post).order_by('-pk')[:3]
    user_already_reviewed = False

    for review in reviews:
        if review.user == request.user:
            user_already_reviewed = True

    return render(
        request,
        'posts_detail.html',
        context = {
            'object': post,
            'reviews': reviews,
            'user_already_reviewed': user_already_reviewed
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


class UserIsReviewOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        # Get review
        review = Review.objects.get(pk=self.kwargs['pk'])
        if self.request.user == review.user:
            return True

        return False

class ReviewUpdateView(LoginRequiredMixin, UserIsReviewOwnerMixin, UpdateView):
    template_name = 'review_update.html'
    form_class = ReviewForm
    model = Review
    success_url = reverse_lazy('posts-page')


class ReviewDeleteView(LoginRequiredMixin, UserIsReviewOwnerMixin, DeleteView):
    template_name = 'review_confirm_delete.html'
    model = Review
    success_url = reverse_lazy('posts-page')


def see_all_reviews_view(request, pk):
    post = Post.objects.get(pk=pk)
    reviews = Review.objects.filter(post=post).order_by('-pk')

    return render(
        request,
        'reviews.html',
        context = {
            'object': post,
            'reviews': reviews,
        }
    )