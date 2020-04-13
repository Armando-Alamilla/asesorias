"""School serializers."""

# Django REST Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Models
from asesorias.schools.models import School


class SchoolSerializer(serializers.Serializer):
    """School serializer."""

    name = serializers.CharField()
    slug_name = serializers.SlugField()
    about = serializers.CharField()
    subjects_offered = serializers.IntegerField()


class CreateSchoolSerializer(serializers.Serializer):
    """Create school serializer."""

    name = serializers.CharField(
        max_length=150,
        validators=[
            UniqueValidator(queryset=School.objects.all())
        ]
    )

    slug_name = serializers.SlugField(
        max_length=40,
        validators=[
            UniqueValidator(queryset=School.objects.all())
        ]
    )

    about = serializers.CharField(
        max_length=255,
        required=False
    )

    def create(self, data):
        """Create school."""
        return School.objects.create(**data)
