# myapp/urls.py
from django.urls import path
from .views import register, user_login,home,logout_request

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('home/', home, name='home'),
    path("logout/", logout_request, name="logout"),
]
