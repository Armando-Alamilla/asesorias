"""Users URLs."""

# Django imports
from django.urls import path

# Views
from asesorias.users.views import UserLoginAPIView

urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name='login')
]
