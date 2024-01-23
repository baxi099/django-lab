from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'address', 'mobile_number', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'address', 'mobile_number')

admin.site.register(CustomUser, CustomUserAdmin)
