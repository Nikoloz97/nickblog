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
    feature_content = models.TextField(max_length=2000)
    feature_image = models.ImageField(upload_to='assets/images', blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
class Content (models.Model):
    TYPE_CHOICES = (('text', 'Text'), ('image', 'Image')) 

    post = models.ForeignKey(Post, related_name='contents', on_delete=models.CASCADE)
    content_type = models.CharField(max_length=5, choices=TYPE_CHOICES)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='assets/images', blank=True, null=True)
    def __str__(self):
        return self.content_type

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=2000)

    def __str__(self):
        return self.content 


