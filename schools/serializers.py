"""school serializers."""

from drf_writable_nested.serializers import WritableNestedModelSerializer

from base.serializers import ContactInfoSerializer, LocationSerializer
from schools.models import School


class SchoolSerializers(WritableNestedModelSerializer):
    """school serializers."""

    location = LocationSerializer(required=False, many=True)
    contact_information = ContactInfoSerializer(required=False, many=True)

    class Meta:
        """meta options."""

        model = School
        exclude = ["created_at", "updated_at"]
