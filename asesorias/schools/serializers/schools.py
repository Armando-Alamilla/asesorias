"""School serializers."""

# Django REST Framework
from rest_framework import serializers

# Model
from asesorias.schools.models import School


class SchoolModelSerializer(serializers.ModelSerializer):
    """School model serializer."""

    class Meta:
        """Meta class."""

        model = School
        fields = (
            'id', 'name', 'slug_name',
            'about', 'picture',
            'subjects_offered',
            'verified', 'is_public'
        )
