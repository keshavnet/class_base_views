from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import PostForm
from django.views import generic

from .models import Post

# Create your views here.

class upload(generic.CreateView):
    form_class = PostForm
    template_name = 'post/add_post.html'
    success_url = '/thanks/'
    




