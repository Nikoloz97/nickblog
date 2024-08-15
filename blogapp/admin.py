from django.contrib import admin

from .models import Post, Content

class ContentInline(admin.TabularInline):
    model = Content
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [
        ContentInline
    ]

admin.site.register(Post, PostAdmin)