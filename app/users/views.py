from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from study_groups.models import StudyGroup

from .models import User, UserProfile, InstructorProfile
from .serializers import UserSerializer, UserProfileSerializer, InstructorProfileSerializer


@permission_classes([IsAuthenticated])
class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@permission_classes([IsAuthenticated])
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


@permission_classes([IsAuthenticated])
class InstructorProfileViewSet(viewsets.ModelViewSet):
    queryset = InstructorProfile.objects.all()
    serializer_class = InstructorProfileSerializer


@permission_classes([IsAuthenticated])
class UserProfileByStudyGroup(APIView):
    def get(self, request, *args, **kwargs):
        group_name = kwargs.get("group", "")
        group = StudyGroup.objects.get(name=group_name)
        user_profiles = UserProfile.objects.filter(group=group.id)
        serializer = UserProfileSerializer(user_profiles, many=True)
        return Response(serializer.data)
