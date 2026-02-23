"""Users app models module."""

import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from users.choices import UserRoleChoices


class User(AbstractUser):
    """Custom user model."""

    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4, db_index=True
    )
    email = models.EmailField(
        unique=True,
        db_index=True,
        error_messages={"unique": "A user with that email already exists."},
    )
    role = models.CharField(max_length=20, choices=UserRoleChoices.choices)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
