"""users urls module."""

from django.urls import path
from .views import UserCreateView

app_name = "users"

urlpatterns = [
    path("auth/register/", UserCreateView.as_view(), name="user-create"),
]
