from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets

    list_filter = UserAdmin.list_filter

    list_display = (
        "username",
        "first_name",
        "last_name",
        "count_following",
        "count_followers",
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
    )


@admin.register(models.UserFollowing)
class UserFollowingAdmin(admin.ModelAdmin):

    list_display = ("following_user", "following_target_user")
