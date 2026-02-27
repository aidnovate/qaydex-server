"""Users views module."""

from abc import ABC, abstractmethod

from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView
from .models import User
from .serializers import UserOutSerializer, UserSerializer, UserLoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken
from dj_rest_auth.views import LoginView


class UserCreateView(CreateAPIView):
    """View for creating a new user."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class BaseLoginView(ABC, LoginView):
    """This class inherits the LoginView from the rest_auth package.
    Django rest auth lib does not support the refresh token
    logic. However,restframework_simplejwt does. Rest auth was
    used because it's based off all-auth which can be used for
    social logins as well as signing in with either username or
    password(of which simplejwt does not support). The two libraries
    were combined to give the required results.
    """

    def get_extra_payload(self):
        """get extra payload for jwt token."""
        return {}

    @abstractmethod
    def login(self):
        """login user."""

    def get_response(self):
        """get response for jwt token."""
        data = {}

        refresh = self.get_token(self.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data.update(self.get_extra_payload())
        return data

@extend_schema(request=UserLoginSerializer, responses=UserOutSerializer)
class UserLoginView(BaseLoginView):
    """View for logging in a user."""

    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]

    def login(self):
        """login user."""
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        return user

    def get_token(self, user):
        """get token for user."""
        return UserSerializer(user).data


class UserLogoutView(APIView):
    """View for logging out a user."""

    def post(self, request):
        """logout user."""
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
