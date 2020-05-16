"""Schools permission classes."""

# Django REST Framework
from rest_framework.permissions import BasePermission

# Models
from asesorias.schools.models import Membership


class IsSchoolAdmin(BasePermission):
    """Allow access only to school admins."""

    def has_object_permission(self, request, view, obj):
        """Varify user have a membership in the object."""
        try:
            Membership.objects.get(
                user=request.user,
                school=obj,
                is_admin=True,
                is_active=True
            )
        except Membership.DoesNotExist:
            return False        
        return True
