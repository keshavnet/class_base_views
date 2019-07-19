from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import PostForm
from django.views import generic

from .models import Post

# Create your views here.

class upload(generic.CreateView):
    form_class = PostForm
    template_name = 'post/add_post.html'
    success_url = '/post/uploadedSuccess/'

class uploadedSuccess(generic.ListView):
    model = Post
    template_name = 'post/uploaded_successfully.html'
   
class postList(generic.ListView):
    posts = Post.objects.all()
    print('----------------------------------')
    print('Posts ---->', Post)
    model = Post
    template_name = 'post/post_list.html'


