"""users serializers."""

from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """user serializer."""

    class Meta:
        """meta options."""

        model = User
        fields = ["username", "email", "password", "id", "role"]
        extra_kwargs = {"password": {"write_only": True}, "id": {"read_only": True}}


class UserLoginSerializer(serializers.Serializer):
    """user login serializer."""

    email = serializers.EmailField()
    password = serializers.CharField(max_length=128)


class UserRegisterSerializer(serializers.ModelSerializer):
    """user register serializer."""

    class Meta:
        """meta options."""

        model = User
        fields = ["username", "email", "password"]


class UserOutSerializer(serializers.Serializer):
    """user serializer."""

    refresh = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)
    users = UserSerializer(read_only=True)
