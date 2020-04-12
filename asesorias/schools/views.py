"""Schools views."""

# Django REST Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Models
from asesorias.schools.models import School


@api_view(['GET'])
def list_schools(request):
    """List schools."""

    schools = School.objects.filter(is_public=True)
    data = []

    for school in schools:
        data.append({
            'name': school.name,
            'slug_name': school.slug_name,
            'about': school.about,
            'subjects_offered': school.subjects_offered,
            'verified': school.verified,
        })

    return Response(data)


@api_view(['POST'])
def create_school(request):
    """Create school."""

    name = request.data['name']
    slug_name = request.data['slug_name']
    about = request.data.get('about', '')

    school = School.objects.create(name=name, slug_name=slug_name, about=about)

    data = {
        'name': school.name,
        'slug_name': school.slug_name,
        'about': school.about,
        'subjects_offered': school.subjects_offered,
        'verified': school.verified,
    }

    return Response(data)
