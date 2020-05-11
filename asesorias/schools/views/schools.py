"""School views."""

# Django REST Framework
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Serializers
from asesorias.schools.serializers import SchoolModelSerializer

# Models
from asesorias.schools.models import School, Membership


class SchoolViewSet(viewsets.ModelViewSet):
    """School view set."""

    serializer_class = SchoolModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Restrict list to public-only."""
        queryset = School.objects.all()
        
        if self.action == 'list':
            return queryset.filter(is_public=True)

        return queryset

    def perform_create(self, serializer):
        """Assign circle admin."""
        school = serializer.save()
        user = self.request.user
        profile = user.profile
        Membership.objects.create(
            user=user,
            profile=profile,
            school=school,
            is_admin=True,
            is_teacher=True,
        )
