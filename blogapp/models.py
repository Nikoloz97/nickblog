from django.db import models

class User (models.Model):
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    display_name = models.CharField(max_length=500)

    def __str__(self):
        return self.username
    
class Post(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=200000)
    image_urls = models.JSONField(default=dict)
    published_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class FeaturePost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=2000)
    image_url = models.CharField(max_length=2000)
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=2000)

    def __str__(self):
        return self.content 


