# blog/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Blog, BlogPost
from django.contrib.auth.forms import UserCreationForm

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['blog_title']

class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['content']

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user