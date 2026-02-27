"""users urls module."""

from django.urls import path
from .views import UserCreateView, UserLogoutView, UserLoginView

app_name = "users"

urlpatterns = [
    path("auth/register/", UserCreateView.as_view(), name="user-create"),
    path("auth/login/", UserLoginView.as_view(), name="user-login"),
    path("auth/logout/", UserLogoutView.as_view(), name="user-logout"),
]
