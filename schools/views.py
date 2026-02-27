"""school views."""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from schools.models import School
from schools.serializers import SchoolSerializers
from base.permissions import IsAdminOrReadOnly
from drf_spectacular.utils import extend_schema


@extend_schema(request=SchoolSerializers, responses=SchoolSerializers(many=True))
class SchoolView(APIView):
    """school view."""

    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        """get all schools."""
        schools = School.objects.all()
        serializer = SchoolSerializers(schools, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """create a school."""
        serializer = SchoolSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(request=SchoolSerializers, responses=SchoolSerializers)
class SchoolDetailView(APIView):
    """school detail view."""

    permission_classes = [IsAdminOrReadOnly]

    def get_object(self, slug):
        """get a single school."""
        try:
            return School.objects.get(slug=slug)
        except School.DoesNotExist:
            return Response(
                {"error": "School not found."}, status=status.HTTP_404_NOT_FOUND
            )

    def get(self, request, slug):
        """get a single school."""
        school = self.get_object(slug)
        serializer = SchoolSerializers(school)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, slug):
        """update a school."""
        school = self.get_object(slug)
        serializer = SchoolSerializers(school, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        """delete a school."""
        school = self.get_object(slug)
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
