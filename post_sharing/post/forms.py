from django import forms
from .models import *


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'image', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols':15})
        }