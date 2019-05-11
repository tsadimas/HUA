from django.shortcuts import render
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'home.html', {})


def auth_login(request):
    return render(request, 'registration/login.html', {})
