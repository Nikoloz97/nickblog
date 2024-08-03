from django.shortcuts import get_object_or_404, render

from .models import Post

def index(request):
    posts = Post.objects.order_by("published_date")
    context = {"posts": posts}
    return render (request, "blogapp/index.html", context)

def post(request, post_id): 
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "polls/post.html", {"post": post})