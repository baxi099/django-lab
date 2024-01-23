Django - Admin Panel :


The Django admin panel is a powerful and customizable interface that allows developers and administrators to manage and interact with data stored in a Django project's database. It is automatically generated based on the models defined in your Django application, making it a convenient tool for performing various administrative tasks without having to create a separate user interface.

The admin site is a built-in Django app that provides a web-based interface for managing models and their data.
It is configured in the project's urls.py file by including admin.site.urls.
The admin site is typically accessible at the /admin/ URL path.

To make a model accessible in the Django admin panel, you need to register it with the admin site.
This is done using the admin.site.register() function in the admin.py file of your app.
The registration process allows Django to generate an admin interface for managing instances of the model.

-------------------Demo Application Step-wise------------------------------------------------------------------

1. Create a new django project.

2. Create an app.

3. Open models.py and paste below code :

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

4. Now, open admin.py and paste the below code :

from django.contrib import admin
from .models import Blog,BlogPost

# Register your models here.
admin.site.register(Blog)
admin.site.register(BlogPost)

5. Add your all to 'INSTALLED_APPS'section in settings.py

6. Run migration commands :
python manage.py makemigrations
python manage.py migrate

7. Now run below command :
python manage.py createsuperuser
provide email and password and create the admin user.

8. Now run the project and go to /admin URL.

9. You will be able to add new Blog, BlogPost and users from this interface. Notice the foreign key relationship between user and blog and blog and BlogPost.
