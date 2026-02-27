"""base model choices."""

from django.db import models
from django.utils.translation import gettext_lazy as _


class GhanaRegionChoices(models.TextChoices):
    """Standard Ghana administrative regions"""

    AHAFO = "AH", _("Ahafo")
    ASHANTI = "AS", _("Ashanti")
    BONO = "BO", _("Bono")
    BONO_EAST = "BE", _("Bono East")
    CENTRAL = "CE", _("Central")
    EASTERN = "EA", _("Eastern")
    GREATER_ACCRA = "GA", _("Greater Accra")
    NORTH_EAST = "NE", _("North East")
    NORTHERN = "NO", _("Northern")
    OTI = "OT", _("Oti")
    SAVANNAH = "SV", _("Savannah")
    UPPER_EAST = "UE", _("Upper East")
    UPPER_WEST = "UW", _("Upper West")
    VOLTA = "VO", _("Volta")
    WESTERN = "WE", _("Western")
    WESTERN_NORTH = "WN", _("Western North")


class PreferredContactMethodChoices(models.TextChoices):
    """Preferred contact method choices for users."""

    PHONE = "phone", _("Phone Call")
    WHATSAPP = "whatsapp", _("WhatsApp")
    EMAIL = "email", _("Email")
    SMS = "sms", _("SMS")
    OTHER = "other", _("Other")
