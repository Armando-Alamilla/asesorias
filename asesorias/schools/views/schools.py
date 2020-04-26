"""School views."""

# Django REST Framework
from rest_framework import viewsets

# Serializers
from asesorias.schools.serializers import SchoolModelSerializer

# Models
from asesorias.schools.models import School


class SchoolViewSet(viewsets.ModelViewSet):
    """School view set."""

    queryset = School.objects.all()
    serializer_class = SchoolModelSerializer
