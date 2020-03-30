"""User model."""

# Django imports
from django.db import models
from django.contrib.auth.models import AbstractUser

# Utilities
from asesorias.utils.models import AsesoriasModel


class User(AsesoriasModel, AbstractUser):
    """User model.
    
    Extend form Django's Abstract User, change the username field
    to email and add some extra fields.
    """

    email = models.EmailField(
        'email address',
        unique=True,
        error_message={
            'unique': 'A user with that email already exists.'
        }
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client status',
        default=True,
        help_text=(
            'Help easily distinguish users and perform queries.'
            'Clients are the main type of user.'
        )
    )

    is_verified = models.BooleanField(
        'verified',
        default=False,
        help_text='Set to true when user have verified its email address.'
    )
