from django.shortcuts import render
from .models import Post


def home(request):
    posts = [
        Post(title="Post 1", content="content of post 1"),
        Post(title="Post 2", content="content of post 2"),
        Post(title="Post 3", content="content of post 3")
    ]
    
    return render(request, 'home.html', {'posts' : posts})