# blog/urls.py
from django.urls import path
from .views import create_blog, create_blog_post,home
from .views import register

from . import views
app_name = "firstapp"


urlpatterns = [
    path('create', create_blog, name='create_blog'),
    path('<int:blog_id>/create_post/', create_blog_post, name='create_blog_post'),
    path('home/', home, name='home'),
    # Add other URL patterns as needed
    path('register/', register, name='register'),
    path("login/", views.login_request, name="login"),
    path("", views.home, name="home"),
    path("logout/", views.logout_request, name="logout"),
]
