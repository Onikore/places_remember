from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm, LoginUserForm, AddUserPost
from .models import UserPosts


def home(request):
    return render(request, 'controller/home.html', {})


def load_profile(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        posts = list(UserPosts.objects.filter(username=request.user))
        context['posts'] = posts

    return render(request, 'controller/profile.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


class AddPost(CreateView):
    form_class = AddUserPost
    template_name = 'controller/add_post.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.username = self.request.user
        user.save()
        return redirect('profile')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'controller/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'controller/login.html'

    def get_success_url(self):
        return reverse_lazy('profile')
