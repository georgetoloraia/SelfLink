from django.contrib import admin

from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "display_name", "locale", "created_at")
    search_fields = ("user__username", "display_name", "user__email")
    list_filter = ("locale",)

