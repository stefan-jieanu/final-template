from django.shortcuts import render
from django.views.generic import DetailView

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