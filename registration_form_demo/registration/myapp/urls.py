# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration_view, name='registration'),
]
