"""Teacher's profile model."""

# Django imports
from django.db import models

# Utilities
from asesorias.utils.models import AsesoriasModel


class TeacherProfile(AsesoriasModel):
    """Teacher's profile model.

    A teacher profile inherits from base profile 
    and holds a statistics data.
    """

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )

    biography = models.TextField(max_length=500, blank=True)

    # Stats
    videos_offered = models.PositiveIntegerField(default=0)

    articles_offered = models.PositiveIntegerField(default=0)

    reputation = models.FloatField(
        default=0.0,
        help_text="Teacher's reputation based on the quality of content that share"
    )

    def __str__(self):
        """Return user's str representation"""
        return str(self.user)
