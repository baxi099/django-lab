# blog/views.py
from django.shortcuts import render, redirect
from .models import Blog,BlogPost

def home(request):
    blogs = Blog.objects.all()
    blog_posts = BlogPost.objects.all()
    return render(request, 'home.html', {'blogs': blogs, 'blog_posts': blog_posts})

