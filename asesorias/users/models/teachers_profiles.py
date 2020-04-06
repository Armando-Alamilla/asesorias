"""Teacher's profile model."""

# Django imports
from django.db import models

# Local models
from .profiles import Profile as BaseProfile


class TeacherProfile(BaseProfile):
    """Teacher's profile model.

    A teacher profile inherits from base profile 
    and holds a statistics data.
    """

    videos_offered = models.PositiveIntegerField(default=0)

    articles_offered = models.PositiveIntegerField(default=0)

    reputation = models.FloatField(
        default=0.0,
        help_text="Teacher's reputation based on the quality of content that share"
    )
