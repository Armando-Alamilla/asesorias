"""Schools admin."""

# Django imports
from django.contrib import admin

# Models
from asesorias.schools.models import School, Membership


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    """School admin."""

    list_display = (
        'slug_name',
        'name',
        'courses_offered',
        'is_public',
        'verified',
        'picture',
    )

    search_fields = ('slug_name', 'name')

    list_filter = (
        'courses_offered',
        'is_public',
        'verified'
    )


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    """Membership admin."""

    list_display = (
        'user',
        'school',
        'is_admin',
        'is_teacher',
        'articles_offered',
        'videos_offered',
        'invited_by',
        'is_active',
    )

    search_fields = ('user', 'school', 'invited_by')

    list_filter = ('is_admin', 'is_teacher', 'is_active')
