"""API views for the users domain."""

from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import UserProfile
from .serializers import UserProfileSerializer


class MeProfileView(generics.RetrieveUpdateAPIView):
    """Retrieve or update the authenticated user's profile."""

    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        profile, _ = UserProfile.objects.get_or_create(user=self.request.user)
        return profile


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def ping(_request):
    """Simple readiness probe for the users API."""

    return Response({"status": "users-ok"})

