from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import SignUpForm
from accounts.models import UserPostRelation


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'login.html'


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'change_password.html'

    # Pagina la care vom fi trimisi dupa ce resetam parola
    success_url = reverse_lazy('home')


class SignUpView(CreateView):
    template_name = 'signup.html'

    # Formularul standard (creat de Django) pentru creat utilizatori noi
    form_class = SignUpForm

    success_url = reverse_lazy('home')


@login_required
def favourites_view(request):
    posts = UserPostRelation.objects.filter(user=request.user)
    return render(
        request,
        'favorites.html',
        context={'posts': posts}
    )

