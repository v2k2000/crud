from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
<<<<<<< HEAD
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)