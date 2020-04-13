"""Schools views."""

# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from asesorias.schools.models import School

# Serializer
from asesorias.schools.serializers import (
    SchoolSerializer,
    CreateSchoolSerializer
)


@api_view(['GET'])
def list_schools(request):
    """List schools."""

    schools = School.objects.filter(is_public=True)
    serializer = SchoolSerializer(schools, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def create_school(request):
    """Create school."""
    
    serializer = CreateSchoolSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    school = serializer.save()

    return Response(CreateSchoolSerializer(school).data)
