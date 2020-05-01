"""Membership model."""

# Django imports
from django.db import models

# Utilities
from asesorias.utils.models import AsesoriasModel


class Membership(AsesoriasModel):
    """Membership model.
    
    A membership is the table that holds the relationship between
    a user and a school.
    """
    
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    school = models.ForeignKey('schools.School', on_delete=models.CASCADE)

    is_admin = models.BooleanField(
        'school admin',
        default=False,
        help_text='School admins can update the school\'s data and change its members.'
    )

    is_teacher = models.BooleanField(
        'school teacher',
        default=False,
        help_text='Teachers can upload content such as videos or articles on school courses.'
    )

    # Invitations
    used_invitations = models.PositiveSmallIntegerField(default=0)
    invited_by = models.ForeignKey(
        'users.User',
        null=True,
        on_delete=models.SET_NULL,
        related_name='invited_by'
    )

    # Stats
    videos_offered = models.PositiveIntegerField(default=0)
    articles_offered = models.PositiveIntegerField(default=0)

    # Status
    is_active = models.BooleanField(
        'active status',
        default=True,
        help_text='Only active users are allowed to interact in the school.'
    )

    def __str__(self):
        """Return username and school."""
        return '@{} at #{}'.format(
            self.user.username,
            self.school.slug_name
        )
