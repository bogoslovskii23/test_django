from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer
import sys
sys.path.append('..')


class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    search_fields = ['name']
    filterset_fields = [key.name for key in Profile._meta.get_fields()]

