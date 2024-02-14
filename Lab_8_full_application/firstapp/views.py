# blog/views.py
from django.shortcuts import render, redirect
from .forms import BlogForm, BlogPostForm
from .models import Blog,BlogPost

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


from .forms import NewUserForm
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, authenticate, logout #add this

def home(request):
    blogs = Blog.objects.all()
    blog_posts = BlogPost.objects.all()
    return render(request, 'home.html', {'blogs': blogs, 'blog_posts': blog_posts})


def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            current_user = request.user

            # Create a new Blog instance and associate it with the current user
            blog = form.save(commit=False)
            blog.user = current_user
            blog.save()
            return redirect("firstapp:home")
    else:
        form = BlogForm()
    return render(request, 'create_blog.html', {'form': form})

def create_blog_post(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.blog = blog
            blog_post.save()
            return redirect('blog_detail', blog_id=blog.id)
    else:
        form = BlogPostForm(initial={'blog': blog})
    return render(request, 'create_blog_post.html', {'form': form, 'blog': blog})




# myapp/views.py



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("firstapp:home")  # Redirect to the home page after registration
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("firstapp:home")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("firstapp:home")