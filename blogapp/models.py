from django.db import models
from django.utils.timezone import now
from .utils.azure_upload import upload_to_azure

class User (models.Model):
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    display_name = models.CharField(max_length=500)

    def __str__(self):
        return self.username
    
class Post(models.Model): 
    # First = DB; second = UI (on admin)
    TYPE_CATEGORIES = (('coding','Coding'), ('health', 'Health'), ('travel', 'Travel'))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=10, choices=TYPE_CATEGORIES, null=True)
    feature_content = models.TextField(max_length=2000) 
    feature_image_url = models.URLField(blank=True, null=True)
    published_date = models.DateField(default=now, null=True, blank=True)
    likes = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
class Image(models.Model):
    file = models.FileField(upload_to='uploads/', blank=True, null=True)  # For local uploads
    caption = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)  # Store Azure Blob URL after upload

    def save(self, *args, **kwargs):
        # Upload file to Azure and set `url` field
        if self.file and not self.url:
            self.url = upload_to_azure(self.file, 'uploaded-image')  # TODO: change this hard-coded directory to post title 
        super(Image, self).save(*args, **kwargs)

    def __str__(self):
        return self.url or "No URL"

class Content(models.Model):
    TYPE_CHOICES = (('header', 'Header'), ('subheader', 'Subheader'), ('text', 'Text'), ('link', 'Link'), ('image', 'Image')) 
    post = models.ForeignKey(Post, related_name='contents', on_delete=models.CASCADE)
    content_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    header = models.TextField(blank=True, null=True)
    subheader = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    link_url = models.TextField(blank=True, null=True)
    link_text = models.TextField(blank=True, null=True)
    image = models.ForeignKey(Image, blank=True, null=True, on_delete=models.SET_NULL)  
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order'] # orders by order field by default
    
    def __str__(self):
        return self.content_type

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=2000)

    def __str__(self):
        return self.content 


