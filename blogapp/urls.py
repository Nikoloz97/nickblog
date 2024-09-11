from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('<str:category>/', views.category_posts, name="categoryPosts"),
    path("contact", views.contact, name="contact"),
    path("post/<int:post_id>/", views.post, name="post_content")
]