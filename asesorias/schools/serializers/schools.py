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
            'name', 'slug_name',
            'about', 'picture',
            'courses_offered',
            'verified', 'is_public'
        )
        read_only_fields = (
            'is_public',
            'verified',
            'courses_offered',
        )
