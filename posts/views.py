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

def detail(request, id):
    post =Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request,'detail.html',context)
=======

    context = {
        'posts': posts,
    }

    return render(request, 'index.html', context)


def detail(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post,
    }

    return render(request, 'detail.html', context)

>>>>>>> 3654344d10e2e0b936df70d1385f45f556f65bf2

def new(request):
    return render(request, 'new.html')

<<<<<<< HEAD
=======

>>>>>>> 3654344d10e2e0b936df70d1385f45f556f65bf2
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    post = Post()
    post.title = title
    post.content = content
    post.save()

    return redirect(f'/posts/{post.id}/')

<<<<<<< HEAD
=======

>>>>>>> 3654344d10e2e0b936df70d1385f45f556f65bf2
def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()

    return redirect('/')

<<<<<<< HEAD
def edit(request, id):
    post = Post.objects.get(id=id)
    
    context = {
        'post': post,
    }
    return render(request, 'edit.html', context)

def update(request, id):
    # 기존정보
    post = Post.objects.get(id=id)
    # 새정보 가져오기
    title = request.GET.get('title')
    content = request.GET.get('content')
    # 기존정보 새정보로 바꾸기
    post.title = title
    post.content = content
    post.save()
    return redirect(f'/posts/{post.id}/')


=======

def edit(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post,
    }

    return render(request, 'edit.html', context)


def update(request, id):
    # 기존정보 가지고 오기
    post = Post.objects.get(id=id)

    # 새로운 정보 가지고오기
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 기존정보를 새로운 정보로 바꾸기
    post.title = title
    post.content = content
    post.save()

    return redirect(f'/posts/{post.id}/')
>>>>>>> 3654344d10e2e0b936df70d1385f45f556f65bf2
