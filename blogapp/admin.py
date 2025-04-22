from django.contrib import admin
from .models import Post
from .forms import PostAdminForm
from .forms import ContentInlineForm
from .utils.azure_upload import upload_to_azure

from .models import Post, Content

class ContentInline(admin.TabularInline):
    model = Content
    form = ContentInlineForm
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [
        ContentInline
    ]
    form = PostAdminForm

    def save_model(self, request, obj, form, change):
        image_file = form.cleaned_data.get('image_file')
        if image_file:
            obj.feature_image_url = upload_to_azure(image_file, obj.title)

        super().save_model(request, obj, form, change)

    def save_related(self, request, form, formsets, change):
        """
        Override save_related to ensure inline Content images are processed.
        """
        super().save_related(request, form, formsets, change)

        for formset in formsets:
            for inline_form in formset.forms:
                if inline_form.cleaned_data.get("image_file"):
                    content_obj = inline_form.instance
                    content_obj.image_url = upload_to_azure(inline_form.cleaned_data["image_file"], content_obj.post.title)
                    content_obj.save()

admin.site.register(Post, PostAdmin)