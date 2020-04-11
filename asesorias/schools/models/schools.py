"""School model."""

# Django imports
from django.db import models

# Utilities
from asesorias.utils.models import AsesoriasModel


class School(AsesoriasModel):
    """School model.

    A school is a private group that have subjects where 
    videos and posts are offered and taken by its members. 
    To join a school a user must receive an unique invitation 
    code from an existing school member.
    """

    name = models.CharField('school name', unique=True, max_length=150)
    slug_name = models.SlugField(unique=True, max_length=40)

    about = models.CharField('school description', max_length=255)
    picture = models.ImageField(upload_to='schools/pictures', blank=True, null=True)

    # Stats
    subjects_offered = models.PositiveIntegerField(default=0)

    verified = models.BooleanField(
        'verified school',
        default=False,
        help_text='verified schools are also recognized as an official school.'
    )

    is_public = models.BooleanField(
        default=True,
        help_text='Visible schools are listed in the main page so everyone know about their existence.'
    )

    def __str__(self):
        """Return school name."""
        return self.name

    class Meta(AsesoriasModel.Meta):
        """Meta class."""

        ordering = ['-subjects_offered']
