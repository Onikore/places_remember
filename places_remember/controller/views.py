from django.shortcuts import render


def home(request):
    return render(request, 'controller/home.html', {})


def profile(request):
    return render(request, 'controller/profile.html', {})


def login(request):
    return render(request, 'controller/login.html', {})
