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
        "count_reviews",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
    )


@admin.register(models.UserFollowing)
class UserFollowingAdmin(admin.ModelAdmin):

    list_display = ("user_id", "following_user_id")

    ordering = ("-user_id",)
