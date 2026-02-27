"""base serializers."""

from rest_framework import serializers
from base.models import ContactInfo, Location


class LocationSerializer(serializers.ModelSerializer):
    """location serializer."""

    class Meta:
        """meta options."""

        model = Location
        exclude = ["created_at", "updated_at"]


class ContactInfoSerializer(serializers.ModelSerializer):
    """contact info serializer."""

    class Meta:
        """meta options."""

        model = ContactInfo
        exclude = ["created_at", "updated_at"]
