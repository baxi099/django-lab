# project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('firstapp.urls')),
    # Add other URL patterns as needed
]
