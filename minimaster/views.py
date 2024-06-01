from django.http import HttpResponse
from django.shortcuts import render
from .data import posts
from .models import Post, Category, Tag


def blog(request):
    posts = Post.objects.all()
    return render(request, 'minimaster/index.html', {'posts': posts})


def category(request, slug):
    return render(request, 'minimaster/category.html')


def post(request, slug):
    data = Post.objects.get(slug=slug)
    return render(request, 'minimaster/post.html', {'post': data})


def dashboard(request):
    return render(request, 'minimaster/dashboard.html')


def add_post(request):
    return render(request, 'minimaster/add_post.html')


def edit_post(request):
    return render(request, 'minimaster/edit_post.html')


def sign_up(request):
    return render(request, 'minimaster/sign_up.html')


def sign_in(request):
    return render(request, 'minimaster/sign_in.html')


def reset_password(request):
    return render(request, 'minimaster/reset_password.html')


def change_password(request):
    return render(request, 'minimaster/change_password.html')

#  Static Views


def about(request):
    return render(request, 'minimaster/about.html')


def contact(request):
    return render(request, 'minimaster/contact.html')
