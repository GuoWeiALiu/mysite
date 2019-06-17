from django.contrib import admin

# Register your models here.
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth', 'phone', 'school', "company", "profession", "address", "aboutme", "photo")
    list_filter = ("phone", 'school', "company", "profession")


admin.site.register(UserProfile, UserProfileAdmin)
