from django import forms
from .models import Post, Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['title', 'content']


class CommentToCommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['title', 'content']
