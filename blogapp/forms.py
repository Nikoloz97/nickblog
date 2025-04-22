from django import forms
from .models import Post
from .models import Content

class PostAdminForm(forms.ModelForm):
    image_file = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = '__all__'

class ContentInlineForm(forms.ModelForm):
    image_file = forms.ImageField(required=False)

    class Meta:
        model = Content
        fields = '__all__'