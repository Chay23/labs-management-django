from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import User, UserProfile, InstructorProfile
from .serializers import UserSerializer, UserProfileSerializer, InstructorProfileSerializer


@permission_classes([IsAuthenticated])
class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


@permission_classes([IsAuthenticated])
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


@permission_classes([IsAuthenticated])
class InstructorProfileViewSet(viewsets.ModelViewSet):
    queryset = InstructorProfile.objects.all()
    serializer_class = InstructorProfileSerializer
