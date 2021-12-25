from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm, LoginUserForm, AddUserPost
from .models import UserPosts


def home(request):
    return render(request, 'controller/home.html', {})


def view_post(request, post_slug):
    post = get_object_or_404(UserPosts, slug=post_slug)
    return render(request, 'controller/view_post.html', {'post': post})


def delete_post(request, post_slug):
    UserPosts.objects.filter(slug=post_slug).delete()
    return load_profile(request)


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
