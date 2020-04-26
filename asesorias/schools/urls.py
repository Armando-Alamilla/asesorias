"""Schools URLs."""

# Django imports
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import schools as school_views


router = DefaultRouter()
router.register(r'schools', school_views.SchoolViewSet, basename='school')

urlpatterns = [
    path('', include(router.urls)),
]
