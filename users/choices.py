"""users model choices."""

from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class UserRoleChoices(TextChoices):
    """User role choices."""

    ADMIN = "admin", _("Admin")
    CLASS_TEACHER = "class_teacher", _("Class Teacher")
    HEAD_TEACHER = "head_teacher", _("Head Teacher")
    PRINCIPAL = "principal", _("Principal")
