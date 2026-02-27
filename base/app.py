"""base app configuration."""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BaseConfig(AppConfig):
    """base app configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "base"
    verbose_name = _("Base")
    verbose_name_plural = _("Bases")
