"""Schools admin."""

# Django imports
from django.contrib import admin

# Models
from asesorias.schools.models import School


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    """School admin."""

    list_display = (
        'slug_name',
        'name',
        'subjects_offered',
        'is_public',
        'verified',
        'picture',
    )

    search_fields = ('slug_name', 'name')

    list_filter = (
        'subjects_offered',
        'is_public',
        'verified'
    )
