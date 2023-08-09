from django.forms import forms
from .models import PostModel


class PostForm(forms.Form):
    class Meta:
        model = PostModel
        exclude = 'author'
