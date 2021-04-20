from rest_framework import viewsets, status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, UserProfile, InstructorProfile
from .serializers import UserSerializer, UserProfileSerializer, InstructorProfileSerializer, UserWithProfileSerializer


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
        group_id = kwargs.get("group_id", "")
        user_profiles = UserProfile.objects.filter(group=group_id)
        serializer = UserProfileSerializer(user_profiles, many=True)
        return Response(serializer.data)


class UserCreateView(APIView):
    permission_classes = []
    authentication_classes = []

    def post(self, request):
        serializer = UserWithProfileSerializer(data=request.data)
        if User.objects.filter(email=request.data["email"]):
            return Response({"details": "Користувач з такою електронною поштою уже зареєстрований"})
        if serializer.is_valid():
            serializer.save()
            response = {
                "email": request.data["email"],
                "first_name": request.data["first_name"],
                "last_name": request.data["last_name"],
                "group": request.data["group"]
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
