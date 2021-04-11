from django import forms

from .models import BlogComment, Blog

class BlogCommentForm(forms.ModelForm):

    class Meta:
        model = BlogComment
        fields = ('description',)

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('title','detail',)

