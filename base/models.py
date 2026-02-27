"""Base models for the application."""

from django.db import models
from base.choices import GhanaRegionChoices, PreferredContactMethodChoices
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


PHONE_REGEX = RegexValidator(
    regex=r"^(?:\+233|0)([235789])[0-9]{8}$",
    message=_("Phone number must be in Ghana format: +233 XX XXX XXXX or 0XX XXX XXXX"),
)


class TimeStampedModel(models.Model):
    """Abstract base model that provides created and updated timestamps."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Location(models.Model):
    """school location model."""

    name = models.CharField(
        max_length=200,
        blank=True,
        help_text=_("e.g. 'Main Campus', 'East Legon Branch', 'Student Hostel'"),
    )
    street_address = models.CharField(max_length=255, blank=True)
    landmark = models.CharField(max_length=255, blank=True, null=True)
    postal_address = models.CharField(
        max_length=100, blank=True, help_text="e.g. P.O. Box AN 1234, Accra"
    )
    region = models.CharField(
        max_length=2,
        choices=GhanaRegionChoices.choices,
        blank=True,
        verbose_name=_("Region"),
    )
    district = models.CharField(max_length=100, blank=True)
    town_city = models.CharField(max_length=100, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    is_primary = models.BooleanField(
        default=False, help_text="Is this the main/primary location?"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """meta class for location model."""

        ordering = ["region", "town_city", "name"]
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")

    def __str__(self):
        """string representation of location."""
        parts = []
        if self.name:
            parts.append(self.name)
        if self.town_city:
            parts.append(self.town_city)
        if self.region:
            parts.append(dict(GhanaRegionChoices.choices).get(self.region, self.region))
        return " - ".join(filter(None, parts)) or "Unnamed Location"

    def full_address(self):
        """Return the full address of the location."""
        parts = [
            self.street_address,
            self.landmark,
            self.town_city,
            self.district,
            dict(GhanaRegionChoices.choices).get(self.region) if self.region else None,
            self.postal_address,
        ]
        return ", ".join(filter(None, parts))


class ContactInfo(models.Model):
    """Reusable contact information block."""

    primary_phone = models.CharField(
        max_length=15,
        validators=[PHONE_REGEX],
        blank=True,
        verbose_name=_("Primary Phone"),
    )
    secondary_phone = models.CharField(
        max_length=15,
        validators=[PHONE_REGEX],
        blank=True,
        null=True,
        verbose_name=_("Secondary / WhatsApp Phone"),
    )
    email = models.EmailField(blank=True, verbose_name=_("Email Address"))
    emergency_contact_name = models.CharField(max_length=150, blank=True)
    emergency_contact_phone = models.CharField(
        max_length=15,
        validators=[PHONE_REGEX],
        blank=True,
        verbose_name=_("Emergency Contact Phone"),
    )
    whatsapp = models.CharField(max_length=15, blank=True, validators=[PHONE_REGEX])
    facebook = models.URLField(blank=True, verbose_name="Facebook Profile")
    twitter_handle = models.CharField(max_length=50, blank=True)
    preferred_contact_method = models.CharField(
        max_length=20,
        default="whatsapp",
        blank=True,
        choices=PreferredContactMethodChoices.choices,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """meta class for contact info model."""

        verbose_name = _("Contact Information")
        verbose_name_plural = _("Contact Information Records")

    def __str__(self):
        """string representation of contact info."""
        return f"{self.primary_phone or self.email or 'No contact'}"

    def clean(self):
        """clean method for contact info model."""
        from django.core.exceptions import ValidationError

        if not any([self.primary_phone, self.email]):
            raise ValidationError(_("At least phone or email is required."))
