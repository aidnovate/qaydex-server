"""Users views module."""

from rest_framework.generics import CreateAPIView
from .models import User
from .serializers import UserSerializer
from rest_framework import permissions


class UserCreateView(CreateAPIView):
    """View for creating a new user."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
