from django.contrib import admin
from .models import Blog,BlogPost


from .models import Blog, BlogPost

class BlogAdmin(admin.ModelAdmin):
     readonly_fields = ('id',)

class BlogPostAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
# Register your models here.
admin.site.register(Blog,BlogAdmin)
admin.site.register(BlogPost,BlogPostAdmin)
