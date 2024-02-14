# blog/models.py
from django.contrib.auth.models import User
from django.db import models

class Blog(models.Model):
    blog_title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.blog_title

class BlogPost(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField()
    
    def __str__(self):
        return f"Post in {self.blog.blog_title}"
