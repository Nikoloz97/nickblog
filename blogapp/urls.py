from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("travel", views.travel, name="travel"),
    path("coding", views.coding, name="coding"),
    path("health", views.health, name="health"),
    path("post/<int:post_id>/", views.post, name="post_content")
]