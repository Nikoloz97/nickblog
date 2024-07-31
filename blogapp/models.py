from django.db import models

class User (models.Model):
    #is this necessary?? If so, how to make they're unique numbers?
    userId = models.IntegerField()

    username = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    display_name = models.CharField(max_length=500)

class Post(models.Model): 
    #is this necessary?? If so, how to make they're unique numbers?
    postId = models.IntegerField()
    #necessary? 
    userId = models.IntegerField()

    title = models.CharField(max_length=200)
    content = models.TextField(max_length=200000)
    published_date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    commentCount = models.IntegerField(default=0)
    

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    #is this necessary?? If so, how to make they're unique numbers?
    commentId = models.IntegerField()
    #necessary? 
    postId = models.IntegerField()
    
    content = models.TextField(max_length=2000)


