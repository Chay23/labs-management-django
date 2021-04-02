from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import UserProfile

from .models import Subject
from .serializers import SubjectSerializer


class SubjectsList(APIView):
    def get(self, request):
        user_profile = UserProfile.objects.get(user=request.user.id)
        subjects = Subject.objects.filter(group=user_profile.group)
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
