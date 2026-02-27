"""school urls."""

from django.urls import path
from schools.views import SchoolView, SchoolDetailView

app_name = "schools"

urlpatterns = [
    path("schools/", SchoolView.as_view(), name="schools"),
    path("schools/<str:slug>/", SchoolDetailView.as_view(), name="school_detail"),
]
