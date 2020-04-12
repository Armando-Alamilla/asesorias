"""Schools URLs."""

# Django imports
from django.urls import path

# Views
from asesorias.schools.views import list_schools, create_school

urlpatterns = [
    path('schools/', list_schools),
    path('schools/create/', create_school),
]
