"""Users app models module."""

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom user model."""
