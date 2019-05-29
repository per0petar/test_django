from django import forms

from .models import Posts
from accounts.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['post_title', 'body']

class RawPostForm(forms.Form):
    post_title      = forms.CharField()
    body            = forms.CharField(widget=forms.Textarea())