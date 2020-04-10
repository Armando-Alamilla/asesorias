"""Subject model."""

# Django imports
from django.db import models

# Utilities
from asesorias.utils.models import AsesoriasModel


class Subject(AsesoriasModel):
    """Subject model."""
    
    name = models.CharField('subject name', max_length=60)
    slug_name = models.SlugField(unique=True, max_length=40)
    picture = models.ImageField(upload_to='subjects/pictures/')

    # Stats
    videos_offered = models.PositiveIntegerField(default=0)
    articles_offered = models.PositiveIntegerField(default=0)

    def __str__(self):
        """Return subject name."""
        return self.name

    class Meta(AsesoriasModel.Meta):
        """Meta class."""

        ordering = ['-articles_offered', '-videos_offered']
