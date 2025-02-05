"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts.views import CustomLoginView, CustomPasswordChangeView, SignUpView, favourites_view
from posts.views import index, posts_view, CreatePostView, add_post_to_user, add_review_view, post_detail_view, \
    ReviewUpdateView, ReviewDeleteView, see_all_reviews_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index, name='home'),
    path('posts/', posts_view, name='posts-page'),
    path('posts/create', CreatePostView.as_view(), name='posts-create'),
    path('posts/<pk>', post_detail_view, name='posts-detail'),

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password', CustomPasswordChangeView.as_view(), name='change-password'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('add-post-to-user/<post_id>', add_post_to_user, name='add-post-to-user'),
    path('favorites/', favourites_view, name='favorites'),
    path('add-review/<post_id>', add_review_view, name='add-review'),
    path('edit-review/<pk>', ReviewUpdateView.as_view(), name='edit-review'),
    path('delete-review/<pk>', ReviewDeleteView.as_view(), name='delete-review'),
    path('reviews/<post_id>', see_all_reviews_view, name='reviews')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
