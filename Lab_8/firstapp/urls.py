# blog/urls.py
from django.urls import path
from .views import home


urlpatterns = [
    path('home/', home, name='home'),
    # Add other URL patterns as needed
]
