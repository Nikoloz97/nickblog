from django.shortcuts import get_object_or_404, render

from .models import Post

def home(request):
    posts = Post.objects.order_by("published_date")
    context = {"posts": posts}
    return render (request, "blogapp/home.html", context)

def post(request, post_id): 
    post = get_object_or_404(Post, pk=post_id)
    context = {"post": post}
    return render(request, "blogapp/post.html", context)