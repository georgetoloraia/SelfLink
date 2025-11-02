"""Data models for the users domain."""

from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    display_name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    avatar = models.URLField(blank=True)
    locale = models.CharField(max_length=32, default="en")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "User profile"
        verbose_name_plural = "User profiles"

    def __str__(self) -> str:  # pragma: no cover - simple repr
        return self.display_name or self.user.get_username()

