"""Student's Profile model."""

# Django imports
from django.db import models

# Utilities
from asesorias.utils.models import AsesoriasModel


class StudentProfile(AsesoriasModel):
    """Profile model.
    
    A profile holds a user's public data 
    like biography and picture
    """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )

    biography = models.TextField(max_length=500, blank=True)

    def __str__(self):
        """Return user's str representation"""
        return str(self.user)
