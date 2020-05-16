"""School views."""

# Django REST Framework
from rest_framework import mixins, viewsets

# Permissions
from rest_framework.permissions import IsAuthenticated
from asesorias.schools.permissions.schools import IsSchoolAdmin

# Serializers
from asesorias.schools.serializers import SchoolModelSerializer

# Models
from asesorias.schools.models import School, Membership


class SchoolViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """School view set."""

    serializer_class = SchoolModelSerializer

    def get_queryset(self):
        """Restrict list to public-only."""
        queryset = School.objects.all()
        
        if self.action == 'list':
            return queryset.filter(is_public=True)

        return queryset

    def get_permissions(self):
        """Assign permissions based on actions."""
        permissions = [IsAuthenticated]
        
        if self.action in ['update', 'partial_update']:
            permissions.append(IsSchoolAdmin)

        return [permission() for permission in permissions]

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
