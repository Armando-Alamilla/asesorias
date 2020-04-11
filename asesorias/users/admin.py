"""User models admin."""

# Django imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from asesorias.users.models import User, StudentProfile, TeacherProfile


class CustomUserAdmin(UserAdmin):
    """User model admin."""

    list_display = (
        'email',
        'username',
        'first_name',
        'last_name',
        'is_client',
        'is_teacher',
        'is_staff'
    )

    list_filter = (
        'is_client',
        'is_teacher',
        'is_staff',
        'created',
        'modified'
    )


@admin.register(StudentProfile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('user', 'picture', 'biography')
    
    search_fields = (
        'user__username',
        'user__email',
        'user__first_name',
        'user__last_name'
    )


@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    """Teacher_profile model admin."""

    list_display = (
        'user',
        'reputation',
        'articles_offered',
        'videos_offered',
        'picture',
        'biography'
    )

    search_fields = (
        'user__username',
        'user__email',
        'user__first_name',
        'user__last_name'
    )

    list_filter = ('reputation', 'articles_offered', 'videos_offered')


admin.site.register(User, CustomUserAdmin)
