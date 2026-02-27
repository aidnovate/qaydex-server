"""schools models."""

from django.db import models
from base.models import TimeStampedModel, Location, ContactInfo
from django.utils.text import slugify


class School(TimeStampedModel):
    """school model."""

    name = models.CharField(max_length=225, null=False)
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, null=True, related_name="school_location"
    )
    contact_information = models.ForeignKey(
        ContactInfo,
        null=True,
        on_delete=models.CASCADE,
        related_name="school_contact_info",
    )
    logo = models.ImageField(upload_to="media/schools/logos")
    slug = models.SlugField(unique=True)

    def __str__(self):
        """school str rep."""
        return self.name

    def save(self, *args, **kwargs):
        """create slug from school name."""
        if not self.slug:
            self.slug = slugify("@" + self.name)
        return super().save(*args, **kwargs)
